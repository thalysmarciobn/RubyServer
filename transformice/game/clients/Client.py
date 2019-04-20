import time

from commons.network.buffer import BufferArray


class Client:

    def __init__(self, session, data, player_code, guest=False):
        self.__data = data
        self.__session = session
        self.__guest = guest
        self.__player_code = player_code
        self.__login_time = time.time()
        self.__room = None
        self.__code = None
        self.redistribute_skills_time = time.time() + 600000

    def send(self, data: BufferArray):
        self.__session.send(data)

    def playerCode(self):
        return self.__player_code

    def isGuest(self):
        return self.__guest

    def data(self):
        return self.__data

    def setRoom(self, room):
        self.__room = room

    def setCode(self, code):
        self.__code = code

    def code(self):
        return self.__code

    def room(self):
        return self.__room
