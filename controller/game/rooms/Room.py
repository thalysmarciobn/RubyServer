

class Room:

    def __init__(self, room_name: str, address: str, room_manager: object):
        self.__name = room_name
        self.__address = address
        self.__room_manager = room_manager
        self.__clients = []

    def name(self):
        return self.__name

    def players(self):
        return len(self.__clients)