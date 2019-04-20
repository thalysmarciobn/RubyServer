

class SessionManager:
    __sessions = []

    @staticmethod
    def append(session: object):
        SessionManager.__sessions.append(session)

    @staticmethod
    def remove(session: object):
        SessionManager.__sessions.remove(session)
        del session

    @staticmethod
    def len():
        return len(SessionManager.__sessions)