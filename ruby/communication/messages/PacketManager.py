import os
import pkgutil
import sys

from ruby.communication.messages import Incoming
from ruby.utils import Logging


class PacketManager:

    def __init__(self):
        self.__packets = dict()
        im_package = "incoming"
        im_package_path = os.path.join(os.path.dirname(__file__), im_package.replace(".", "\\"))
        for _, name, __ in pkgutil.iter_modules([im_package_path]):
            package_name = __package__ + "." + im_package + "." + name
            exec("import " + package_name)
            im_modules = sys.modules[package_name]
            for module in dir(im_modules):
                if not module.startswith("IM"): continue
                module_obj = getattr(im_modules, module)
                if Incoming.Incoming in module_obj.mro()[1:]:
                    self.__add__(module_obj())
        Logging.info(f"Packets loaded: {len(self.__packets)}")

    def __add__(self, incoming):
        code = incoming.tokens[1] + (incoming.tokens[0] << 8)
        if not self.__packets.__contains__(code):
            self.__packets[code] = incoming
            Logging.packet("Registered", f"packet: {incoming.tokens} with opcode: {code}")
        else:
            Logging.packet("Failed", f"can't register: {incoming.tokens}")

    def __contains__(self, code):
        return self.__packets.__contains__(code)

    def get(self, code):
        return self.__packets.get(code)
