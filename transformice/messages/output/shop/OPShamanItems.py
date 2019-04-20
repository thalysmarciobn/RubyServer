from commons.communication.Output import Output


class OPShamanItems(Output):
    tokens = [20, 27]

    def __init__(self, items: list, equipped: list):
        super().__init__()
        self.bufferArray.writeShort(len(items))
        for item in items:
            if "_" in item:
                item_info = item.split("_")
                real_item = item_info[0]
                item_customs = item_info[1] if len(item_info) >= 2 else ""
                real_customs = [] if item_customs == "" else item_customs.split("+")
                self.bufferArray.writeShort(int(real_item))
                self.bufferArray.writeBool(item in equipped)
                self.bufferArray.writeByte(len(real_customs) + 1)
                for custom in real_customs:
                    self.bufferArray.writeInt(int(custom, 16))
            else:
                self.bufferArray.writeShort(item)
                self.bufferArray.writeBool(item in equipped)
                self.bufferArray.writeByte(0)
