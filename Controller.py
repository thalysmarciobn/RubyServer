import os

from controller.bulle.BulleManager import BulleManager
from controller.console.TitleConsole import TitleConsole
from controller.rpc.RpcManager import RpcManager


class Controller:
    __rpc_host = "127.0.0.1"
    __rpc_port = 8000

    def __init__(self):
        RpcManager.bind(self.__rpc_host, self.__rpc_port)
        RpcManager.register()
        RpcManager.run()
        TitleConsole.build()
        BulleManager.build()


if __name__ == "__main__":
    os.system("title Loading...")
    Controller = Controller()
