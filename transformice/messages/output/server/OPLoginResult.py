from commons.communication.Output import Output


class OPLoginResult(Output):
    tokens = [26, 12]

    def __init__(self, result: int, complement: str):
        super().__init__()
        self.bufferArray.writeByte(result)
        self.bufferArray.writeUTF(complement)
        self.bufferArray.writeUTF("")
