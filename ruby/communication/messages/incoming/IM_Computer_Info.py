from ruby.communication.messages.Incoming import Incoming


class IM_Computer_Info(Incoming):
    tokens = [28, 17]

    def dispatch(self, Session, BufferArray):
        pass
