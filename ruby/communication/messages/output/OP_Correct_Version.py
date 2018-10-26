from ruby.communication.messages.Output import Output


class OP_Correct_Version(Output):
    output = [26, 3]

    def __init__(self, authKey, lastPacketID):
        self.bufferArray.writeInt(0)  # players online
        self.bufferArray.writeByte(lastPacketID)
        self.bufferArray.writeUTF("br")
        self.bufferArray.writeUTF("br")
        self.bufferArray.writeInt(authKey)
