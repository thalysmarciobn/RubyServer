from commons.communication.Output import Output


class OPRoomGame(Output):
    tokens = [7, 1]

    def __init__(self, game: int):
        super().__init__()
        self.bufferArray.writeByte(game)
