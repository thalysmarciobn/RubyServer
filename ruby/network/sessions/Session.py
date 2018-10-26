import asyncore
import random

from ruby import Controller
from ruby.network.buffer.BufferArray import BufferArray
from ruby.network.buffer.Encoder import Encoder
from ruby.utils import Logging
from ruby.utils.Language import Language


class Session(asyncore.dispatcher_with_send):

    def __init__(self, socket):
        super().__init__(socket)
        Controller.session_manager.append(self)
        self.__socket = socket
        self.__disposed = False
        self.__client = None
        self.__encoder = Encoder()
        self.language = Language(0)
        self.lastPacketID = 0
        self.authKey = random.randrange(0xFFFF)

    def handle_read(self):
        if self.__disposed:
            return
        self.out_buffer = self.recv(1024)
        if not self.out_buffer:
            self.disconnect()
            return
        if self.out_buffer[0] == 60 and self.__client is None:
            self.send(
                "<cross-domain-policy><allow-access-from domain=\"*\" to-ports=\"*\" /></cross-domain-policy>")
            self.disconnect()
            return
        length = len(self.out_buffer)
        if length < 5:
            return
        buffer = BufferArray(self.out_buffer)
        sizeByte = buffer.readByte()
        if sizeByte < 1 or sizeByte > 3:
            return
        packetLen = buffer.readByte() if sizeByte == 1 else buffer.readShort() if sizeByte == 2 else ((
                                                                                                                  buffer.readByte() & 0xFF) << 16) | (
                                                                                                                 (
                                                                                                                             buffer.readByte() & 0xFF) << 8) | (
                                                                                                                 buffer.readByte() & 0xFF) if sizeByte == 3 else 0
        fullPacketLen = packetLen + sizeByte + 2
        if packetLen == 0 or length < fullPacketLen:
            return
        packetId = buffer.readByte()
        if packetId != self.lastPacketID:
            self.disconnect()
            return
        self.lastPacketID = (packetId + 1) % 100
        code1 = buffer.readByte()
        code2 = buffer.readByte()
        opcodes = code2 + (code1 << 8)
        if Controller.packet_manager.__contains__(opcodes):
            Controller.packet_manager.get(opcodes).dispatch(self, buffer)
        else:
            Logging.alert("Packet not found: [" + str(code1) + ", " + str(code2) + "] with opcode: " + str(opcodes))

    def writable(self):
        if not self.__disposed:
            return True

    def send(self, data):
        self.socket.send(self.__encoder.encoder(data))

    def disconnect(self):
        if not self.__disposed:
            Controller.session_manager.remove(self)
            self.__disposed = True
            self.close()
