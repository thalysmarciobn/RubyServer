import random
import sys
import threading
import time

from commons.util import Logging


class BulleManager:
    __servers = {}
    __build = False
    __loop_thread = None
    __last_player_code = 0
    __sessions = {}

    @staticmethod
    def build():
        if not BulleManager.__build and BulleManager.__loop_thread is None:
            Logging.info("Bulle controller working")
            BulleManager.__loop_thread = threading.Thread(target=BulleManager.__loop, name="bulle", daemon=True)
            BulleManager.__build = True
            BulleManager.__loop_thread.start()

    @staticmethod
    def __loop():
        while BulleManager.__build:
            remove = []
            for address, data in BulleManager.__servers.items():
                alive = data.get("alive")
                if int(round(alive * 1000)) <= int(round(time.time() * 1000)) - 10000:
                    remove.append(address)
            for address in remove:
                BulleManager.__remove(address)
            time.sleep(5)

    @staticmethod
    def servers():
        return len(BulleManager.__servers)

    @staticmethod
    def sessions():
        return len(BulleManager.__sessions)

    @staticmethod
    def random():
        if len(BulleManager.__servers) > 0:
            return random.choice(BulleManager.__servers)
        return ""

    @staticmethod
    def removeSession(code: int):
        if code in BulleManager.__sessions:
            BulleManager.__sessions.pop(code)

    @staticmethod
    def getSession(code: int):
        if code in BulleManager.__sessions:
            return BulleManager.__sessions.get(code)
        return None

    @staticmethod
    def generateCode(client: object):
        BulleManager.__last_player_code += 1 % sys.maxsize
        client.setCode(BulleManager.__last_player_code)
        BulleManager.__sessions.update({BulleManager.__last_player_code: client})
        return BulleManager.__last_player_code

    @staticmethod
    def __remove(address: str):
        if BulleManager.__build and address in BulleManager.__servers:
            BulleManager.__servers.pop(address)
            Logging.bulle(address, f"Removed bulle connection.")

    @staticmethod
    def update(address: str):
        if BulleManager.__build:
            if address not in BulleManager.__servers:
                Logging.bulle(address, f"New bulle connection")
            BulleManager.__servers.update({address: {"alive": time.time()}})