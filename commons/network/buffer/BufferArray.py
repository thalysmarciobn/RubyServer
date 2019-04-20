import struct


class BufferArray:
    def __init__(self, data=b""):
        self.bytes = data

    def writeBool(self, data: bool):
        self.bytes += struct.pack('!?', bool(data))

    def writeByte(self, data: int):
        self.bytes += struct.pack('!B', int(data))

    def writeBytes(self, data):
        self.bytes += data

    def writeShort(self, data: int):
        self.bytes += struct.pack('!H', int(data))

    def writeInt(self, data: int):
        self.bytes += struct.pack('!I', int(data))

    def writeLong(self, data: int):
        self.bytes += struct.pack('!Q', int(data))

    def writeUTF(self, data: str):
        data = data.encode()
        length = len(data)
        self.bytes += struct.pack('!H', length)
        self.bytes += data

    def readBool(self):
        data = struct.unpack('!?', self.bytes[:1])[0]
        self.bytes = self.bytes[1:]
        return data

    def readByte(self):
        data = struct.unpack('!B', self.bytes[:1])[0]
        self.bytes = self.bytes[1:]
        return data

    def readBytes(self, length):
        data = self.bytes[:length]
        self.bytes = self.bytes[length:]
        return data

    def readShort(self):
        data = struct.unpack('!H', self.bytes[:2])[0]
        self.bytes = self.bytes[2:]
        return data

    def readInt(self):
        data = struct.unpack('!I', self.bytes[:4])[0]
        self.bytes = self.bytes[4:]
        return data

    def readLong(self):
        data = struct.unpack('!Q', self.bytes[:8])[0]
        self.bytes = self.bytes[8:]
        return data

    def readUTF(self):
        length = struct.unpack('!H', self.bytes[:2])[0]
        data = self.bytes[2:(length + 2)]
        self.bytes = self.bytes[(2 + length):]
        return data.decode()

    def toByteArray(self):
        return self.bytes

    def __len__(self):
        return len(self.bytes)

    def available(self):
        return len(self.bytes) > 0
