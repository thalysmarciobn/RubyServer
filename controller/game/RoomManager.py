from commons.util import Logging
from controller.bulle.BulleManager import BulleManager
from controller.game.rooms.Room import Room


class RoomManager:
    __rooms = {}

    @staticmethod
    def enter(language_code: str, name: str, code: int):
        room_name = f"{language_code}-{name}"
        if room_name not in RoomManager.__rooms:
            bulle = BulleManager.random()
            room = Room(room_name, bulle, RoomManager)
            RoomManager.__rooms.update({room_name: room})
            Logging.info(f"[{room.name()}] creating room with bulle: {bulle}")
        else:
            room = RoomManager.__rooms.get(room_name)

    @staticmethod
    def remove(name):
        if name in RoomManager.__rooms:
            RoomManager.__rooms.pop(name)
            Logging.info(f"[{name}] room removed")

    @staticmethod
    def len():
        return len(RoomManager.__rooms)