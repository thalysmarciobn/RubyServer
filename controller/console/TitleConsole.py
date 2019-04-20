import os
import threading
import time

from controller.bulle.BulleManager import BulleManager
from controller.game.RoomManager import RoomManager


class TitleConsole:
    __build = False
    __loop_thread = None

    @staticmethod
    def build():
        if not TitleConsole.__build and TitleConsole.__loop_thread is None:
            TitleConsole.__loop_thread = threading.Thread(target=TitleConsole.__loop, name="title_console", daemon=True)
            TitleConsole.__build = True
            TitleConsole.__loop_thread.start()

    @staticmethod
    def __loop():
        while TitleConsole.__build:
            os.system(f"title Controller: bulles {BulleManager.servers()}, rooms {RoomManager.len()}, sessions {BulleManager.sessions()}")
            time.sleep(5)
