from commons.communication.Output import Output


class OPTime(Output):
    tokens = [28, 2]

    def __init__(self, time: int):
        super().__init__()
        self.bufferArray.writeInt(time)
