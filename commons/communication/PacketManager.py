

class PacketManager:
    __packets = dict()

    @staticmethod
    def register(incoming):
        code = incoming.tokens[1] + (incoming.tokens[0] << 8)
        if code not in PacketManager.__packets:
            PacketManager.__packets.update({code: incoming})

    @staticmethod
    def contains(code):
        return code in PacketManager.__packets

    @staticmethod
    def get(code):
        return PacketManager.__packets.get(code)

    @staticmethod
    def len():
        return len(PacketManager.__packets)
