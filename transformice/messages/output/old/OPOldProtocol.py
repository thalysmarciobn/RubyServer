from commons.communication.Output import Output


class OPOldProtocol(Output):
    tokens = [1, 1]

    def __init__(self, identifiers: list, values: str):
        super().__init__()
        self.bufferArray.writeShort(len(identifiers) + len(values))
        for identifier in identifiers:
            self.bufferArray.writeByte(identifier)
        #self.bufferArray.writeUTF(values.split("\x01"))
