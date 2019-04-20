import asyncore
import socket

from bulle.game import ClientManager
from commons.communication.PacketManager import PacketManager
from commons.communication.Rules import Rules
from bulle.network.SessionManager import SessionManager
from commons.network.buffer.BufferArray import BufferArray
from commons.util import Logging
from commons.util.Enum.Language import Language


class Session(asyncore.dispatcher):

    def __init__(self, client: socket, address):
        super().__init__(client)
        self.ip_address = address[0]
        self.__disposed = False
        self.client = None
        self.language = Language(0)
        self.last_packet_id = 0
        self.out_buffer = b""
        SessionManager.append(self)

    def handle_read(self):
        if self.__disposed:
            return
        data = self.recv(1024)
        if not data:
            self.disconnect()
            return
        if data == b'<policy-file-request/>\x00' and self.client is None:
            self.send("<cross-domain-policy><allow-access-from domain=\"*\" to-ports=\"*\" /></cross-domain-policy>")
            self.disconnect()
            return
        if len(data) <= 0:
            self.disconnect()
            return
        message = BufferArray(data)
        self.out_buffer += data
        sizeBytes = message.readByte()
        if sizeBytes == 1:
            length = message.readByte()
        elif sizeBytes == 2:
            length = message.readShort()
        elif sizeBytes == 3:
            length = message.readInt()
        else:
            length = 0
        if length <= 0:
            self.disconnect()
            return
        packetId = message.readByte()
        if len(message) != length:
            self.disconnect()
            return
        if packetId != self.last_packet_id:
            self.disconnect()
            return
        self.last_packet_id = (self.last_packet_id + 1) % 100
        code1 = message.readByte()
        code2 = message.readByte()
        opcodes = code2 + (code1 << 8)
        if PacketManager.contains(opcodes):
            incoming = PacketManager.get(opcodes)
            if incoming.rule == Rules.session and self.client is None:
                dispatch = True
            elif incoming.rule == (
                    Rules.sessionAndClient or Rules.onlyClient) and self.client is not None:
                dispatch = True
            else:
                dispatch = False
            if dispatch:
                incoming.dispatch(self, message)
        else:
            Logging.alert(f"Packet not found: [{code1}, {code2}] with opcode: {opcodes}")

    def writable(self):
        return not self.__disposed

    def handle_close(self):
        self.disconnect()

    def send(self, message: object):
        if type(message) is str:
            self.socket.send(message.encode())
        else:
            tokens = message.tokens
            buffer_array = message.bufferArray
            packet = BufferArray()
            length = len(buffer_array) + len(tokens)
            if length <= 0xFF:
                packet.writeByte(1)
                packet.writeByte(length)
            elif length <= 0xFFFF:
                packet.writeByte(2)
                packet.writeShort(length)
            elif length <= 0xFFFFFF:
                packet.writeByte(3)
                packet.writeLong(length)
            else:
                return
            for token in tokens:
                packet.writeByte(token)
            packet.writeBytes(buffer_array.toByteArray())
            self.socket.send(packet.toByteArray())

    def disconnect(self):
        if not self.__disposed:
            self.__disposed = True
            if self.client is not None:
                ClientManager.remove(self.client)
            self.close()
            SessionManager.remove(self)
