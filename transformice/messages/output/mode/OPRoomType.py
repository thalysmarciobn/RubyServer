from commons.communication.Output import Output


class OPRoomType(Output):
    tokens = [7, 30]

    def __init__(self, type: int):
        super().__init__()
        self.bufferArray.writeByte(type)
