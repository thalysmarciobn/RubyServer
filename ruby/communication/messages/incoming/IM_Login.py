from ruby.communication.messages.Incoming import Incoming
from ruby.utils.Language import Language


class IM_Login(Incoming):
    tokens = [26, 8]

    def dispatch(self, Session, BufferArray):
        pass
