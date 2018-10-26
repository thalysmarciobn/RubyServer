from ruby.utils import Logging

class PacketManager():

    def __init__(self):
        self.__packets = dict()

    def __len__(self):
        return len(self.__packets)

    def add(self, Incoming):
        code = Incoming.tokens[1] + (Incoming.tokens[0] << 8);
        if not self.__packets.__contains__(code):
            self.__packets[code] = Incoming
            Logging.packet("Registered", "packet: " + str(Incoming.tokens) + " with opcode: " + str(code))
        else:
            Logging.packet("Failed", "can't register: " + str(Incoming.tokens))

    def __contains__(self, code):
        return self.__packets.__contains__(code)

    def get(self, code):
        return self.__packets.get(code)