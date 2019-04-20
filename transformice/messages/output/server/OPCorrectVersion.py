from commons.communication.Output import Output


class OPCorrectVersion(Output):
    tokens = [26, 3]

    def __init__(self, players: int, flag: str, last_packet_id: int, auth_key: int, auth_key_login: int):
        super().__init__()
        self.bufferArray.writeInt(players)
        self.bufferArray.writeByte(last_packet_id)
        self.bufferArray.writeUTF(flag.lower())
        self.bufferArray.writeUTF(flag.lower())
        self.bufferArray.writeInt(auth_key)
        self.bufferArray.writeInt(auth_key_login)
