from abc import abstractmethod


class Incoming:
    tokens = []

    @abstractmethod
    def dispatch(self, session, buffer_array): raise NotImplementedError
