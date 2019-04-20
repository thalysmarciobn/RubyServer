import threading
from xmlrpc.server import SimpleXMLRPCServer

from commons.util import Logging
from controller.rpc.RpcFunctions import RpcFunctions


class RpcManager:
    __loop_thread = None
    __running = False
    __rpc = None

    @staticmethod
    def bind(host, port):
        if not RpcManager.__running:
            Logging.info(f"RPC server on port: {port}")
            RpcManager.__rpc = SimpleXMLRPCServer((host, port), logRequests=False, allow_none=True)

    @staticmethod
    def register():
        if not RpcManager.__running:
            Logging.info(f"Registering functions in RPC")
            RpcManager.__rpc.register_function(RpcFunctions.updateBulle, "updateBulle")
            RpcManager.__rpc.register_function(RpcFunctions.enterRoom, "enterRoom")
            RpcManager.__rpc.register_function(RpcFunctions.getPlayerDataByCode, "getPlayerDataByCode")

    @staticmethod
    def run():
        if not RpcManager.__running:
            RpcManager.__loop_thread = threading.Thread(target=RpcManager.__rpc.serve_forever, name="rpc")
            RpcManager.__loop_thread.start()
            Logging.info(f"RPC server working on a dedicated thread")
            RpcManager.__running = True

    @staticmethod
    def shutdown():
        if RpcManager.__running and RpcManager.__loop_thread is not None:
            RpcManager.__rpc.shutdown()
            RpcManager.__loop_thread.join()
            RpcManager.__running = False
