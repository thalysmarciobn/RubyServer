from abc import abstractmethod


class Incoming:
    tokens = []

    @abstractmethod
    def dispatch(self, Session, BufferArray): raise NotImplementedError
