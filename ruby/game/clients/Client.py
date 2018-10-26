class Client():

    def __init__(self, session):
        self.__session = session

    def send(self, data):
        self.__session.send(data)
