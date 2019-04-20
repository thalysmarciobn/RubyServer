from bulle.game.rooms.Room import Room
from commons.util import Logging


class RoomManager:
    __rooms = {}

    @staticmethod
    def enter(client: object, room_name: str):
        if room_name not in RoomManager.__rooms:
            room = Room(room_name, RoomManager)
            RoomManager.__rooms.update({room_name: room})
            Logging.info(f"[{room.name()}] creating room...")
        else:
            room = RoomManager.__rooms.get(room_name)
        client.setRoom(room)
        room.enter(client)