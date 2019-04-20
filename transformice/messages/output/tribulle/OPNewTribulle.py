from commons.communication.Output import Output


class OPNewTribulle(Output):
    tokens = [60, 4]

    def __init__(self, enabled: bool):
        super().__init__()
        self.bufferArray.writeBool(enabled)
