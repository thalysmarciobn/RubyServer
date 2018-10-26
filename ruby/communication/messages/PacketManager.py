import inspect
import os
import pkgutil
import sys

from ruby.communication.messages import Incoming
from ruby.utils import Logging


class PacketManager:

    def __init__(self):
        self.__packets = dict()
        IMPackage = "incoming"
        IMPackagePath = os.path.join(os.path.dirname(__file__), IMPackage.replace(".", "\\"))
        for _, name, __ in pkgutil.iter_modules([IMPackagePath]):
            packageName = __package__ + "." + IMPackage + "." + name
            exec("import " + packageName)
            IMModules = sys.modules[packageName]
            for module in dir(IMModules):
                if not module.startswith("IM"): continue
                moduleObj = getattr(IMModules, module)
                if Incoming.Incoming in moduleObj.mro()[1:]:
                    self.__add__(moduleObj())
        Logging.info("Packets loaded: " + str(len(self.__packets)))

    def __add__(self, Incoming):
        code = Incoming.tokens[1] + (Incoming.tokens[0] << 8)
        if not self.__packets.__contains__(code):
            self.__packets[code] = Incoming
            Logging.packet("Registered", "packet: " + str(Incoming.tokens) + " with opcode: " + str(code))
        else:
            Logging.packet("Failed", "can't register: " + str(Incoming.tokens))

    def __contains__(self, code):
        return self.__packets.__contains__(code)

    def get(self, code):
        return self.__packets.get(code)
