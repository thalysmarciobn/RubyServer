import struct

class BufferArray:
    def __init__(self, data=b""):
        if type(data) == bytes:
            self.bytes = data
        elif type(data) == str:
            self.bytes = data.encode()
        else:
            self.bytes = b""

    def write(self, data):
        self.bytes += bytes(data, 'utf-8')

    def writeBool(self, data):
        self.bytes += struct.pack('!?', bool(data))

    def writeByte(self, data):
        self.bytes += struct.pack('!B', int(data))

    def writeBytes(self, data):
        self.bytes += data

    def writeShort(self, data):
        self.bytes += struct.pack('!H', int(data))

    def writeInt(self, data):
        self.bytes += struct.pack('!I', int(data))

    def writeLong(self, data):
        self.bytes += struct.pack('!Q', int(data))

    def writeUTF(self, data):
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
        self.bytes = self.byte[8:]
        return data

    def readUTF(self):
        length = struct.unpack('!H', self.bytes[:2])[0]
        data = self.bytes[2:(length + 2)]
        self.bytes = self.bytes[(2 + length):]
        return data.decode()

    def toByteArray(self):
        return self.bytes

    def length(self):
        return len(self.bytes)

    def bytesAvailable(self):
        return len(self.bytes) > 0