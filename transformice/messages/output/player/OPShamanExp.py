from commons.communication.Output import Output


class OPShamanExp(Output):
    tokens = [8, 8]

    def __init__(self, level: int, exp: int, exp_next_level: int):
        super().__init__()
        self.bufferArray.writeShort(level)
        self.bufferArray.writeInt(exp)
        self.bufferArray.writeInt(exp_next_level)
