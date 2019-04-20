from abc import abstractmethod


class Incoming:
    tokens = []
    rule = None

    @abstractmethod
    def dispatch(self, session, buffer_array): raise NotImplementedError
