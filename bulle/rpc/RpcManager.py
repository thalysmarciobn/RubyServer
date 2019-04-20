import time
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
    def updateBulle(host: str):
        try:
            RpcManager.__proxy.updateBulle(host)
            if not RpcManager.__connected:
                Logging.bulle(host, "Reconnected to main server")
                RpcManager.__connected = True
        except ConnectionRefusedError:
            Logging.bulle(host, "Trying reconnect to main server")
            RpcManager.__connected = False