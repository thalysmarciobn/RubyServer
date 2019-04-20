from commons.communication.Output import Output


class OPEnterRoom(Output):
    tokens = [5, 21]

    def __init__(self, room_name: str):
        super().__init__()
        self.bufferArray.writeBool(room_name.startswith("*") or room_name.startswith(str(chr(3))))
        self.bufferArray.writeUTF(room_name)
