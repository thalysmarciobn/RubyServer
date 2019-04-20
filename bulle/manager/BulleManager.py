import threading
import time

from bulle.rpc.RpcManager import RpcManager


class BulleManager:
    __build = False
    __loop_thread = None
    __host = "127.0.0.1"

    @staticmethod
    def build():
        if not BulleManager.__build and BulleManager.__loop_thread is None:
            BulleManager.__loop_thread = threading.Thread(target=BulleManager.__loop, name="bulle", daemon=True)
            BulleManager.__build = True
            BulleManager.__loop_thread.start()

    @staticmethod
    def __loop():
        while BulleManager.__build:
            RpcManager.updateBulle(BulleManager.__host)
            time.sleep(5)