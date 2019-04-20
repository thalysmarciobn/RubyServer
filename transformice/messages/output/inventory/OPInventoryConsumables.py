from commons.communication.Output import Output


class OPShamanExp(Output):
    tokens = [31, 1]

    def __init__(self, consumables: list):
        super().__init__()
        self.bufferArray.writeShort(len(consumables()))
        for consumable in consumables:
            self.bufferArray.writeShort(consumable[0])
            self.bufferArray.writeByte(consumable[1])
            self.bufferArray.writeByte(consumable[2])
            self.bufferArray.writeBool(False)
            self.bufferArray.writeBool(consumable[3])
            self.bufferArray.writeBool(consumable[3])
            self.bufferArray.writeBool(not consumable[3])
            self.bufferArray.writeBool(consumable[4])
            self.bufferArray.writeBool(False)
            self.bufferArray.writeBool(not consumable[5] == "")
            if not consumable[5] == "":
                self.bufferArray.writeUTF(consumable[5])
            self.bufferArray.writeByte(consumable[6] + 1)
