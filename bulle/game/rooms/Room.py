

class Room:

    def __init__(self, room_name: str, room_manager: object):
        self.__name = room_name
        self.__room_manager = room_manager
        self.__clients = []

