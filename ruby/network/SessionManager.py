class SessionManager:

    def __init__(self):
        self.__sessions = []

    def append(self, session):
        self.__sessions.append(session)

    def remove(self, session):
        self.__sessions.remove(session)

    def __len__(self):
        return len(self.__sessions)

    def __contains__(self, session):
        return session in self.__sessions