import asyncore
import random

from ruby import Controller
from ruby.network.buffer.BufferArray import BufferArray
from ruby.network.buffer.Encoder import Encoder
from ruby.utils import Logging
from ruby.utils.Language import Language


class Session(asyncore.dispatcher_with_send):

    def __init__(self, socket, address):
        super().__init__(socket)
        Controller.session_manager.append(self)
        self.__socket = socket
        self.__disposed = False
        self.__client = None
        self.__encoder = Encoder()
        self.ipAddress = address[0]
        self.language = Language(0)

    def handle_read(self):
        if self.__disposed:
            return

        out_buffer = self.recv(1024)
        if not out_buffer:
            self.disconnect()
            return

        length = len(out_buffer)

        if length < 2:
            return
        buffer = BufferArray(out_buffer)

        code1 = buffer.readByte()
        code2 = buffer.readByte()
        opcodes = code2 + (code1 << 8)
        if Controller.packet_manager.__contains__(opcodes):
            Controller.packet_manager.get(opcodes).dispatch(self, buffer)
        else:
            Logging.alert(f"Packet not found: [{code1}, {code2}] with opcode: {opcodes}")

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
