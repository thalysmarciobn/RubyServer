import xmlrpc.client

from commons.util import Logging


class RpcManager:
    __connected = False
    __proxy = None

    __rpc_host = "127.0.0.1"
    __rpc_port = 8000

    @staticmethod
    def connect():
        if not RpcManager.__connected:
            with xmlrpc.client.ServerProxy(f"http://{RpcManager.__rpc_host}:{RpcManager.__rpc_port}/") as proxy:
                RpcManager.__proxy = proxy
                RpcManager.__connected = True

    @staticmethod
    def enterRoom(language_code: str, code: int, name: str):
        RpcManager.__proxy.enterRoom(language_code, code, name)