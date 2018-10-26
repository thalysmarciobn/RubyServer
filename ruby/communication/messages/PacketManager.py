import inspect
import sys

from ruby.communication.messages import *
from ruby.communication.messages import Incoming
from ruby.utils import Logging

class PacketManager():

    def __init__(self):
        self.__packets = dict()
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj) and Incoming.Incoming in obj.mro():
                self.__add__(obj)

    def __len__(self):
        return len(self.__packets)

    def __add__(self, Incoming):
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