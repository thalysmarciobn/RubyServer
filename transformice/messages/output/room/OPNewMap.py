from commons.communication.Output import Output


class OPNewMap(Output):
    tokens = [5, 2]

    def __init__(self, mapCode: int, players: int, round_code: int, map_xml: str, map_name: str, map_category: int, map_inverted: bool):
        super().__init__()
        xml = 0 if map_xml is "" or None else map_xml.encode("zlib")
        self.bufferArray.writeInt(mapCode)
        self.bufferArray.writeShort(players)
        self.bufferArray.writeByte(round_code)
        self.bufferArray.writeInt(len(xml))
        self.bufferArray.writeBytes(xml)
        self.bufferArray.writeUTF(map_name)
        self.bufferArray.writeByte(map_category)
        self.bufferArray.writeBoolean(map_inverted)
