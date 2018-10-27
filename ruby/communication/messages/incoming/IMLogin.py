from ruby.communication.messages.Incoming import Incoming


class IMLogin(Incoming):
    tokens = [26, 8]

    def dispatch(self, session, buffer_array):
        pass
