from commons.communication.Output import Output


class OPBulle(Output):
    tokens = [44, 1]

    def __init__(self, player_code: int, address: str):
        super().__init__()
        self.bufferArray.writeInt(player_code)
        self.bufferArray.writeUTF(address)
