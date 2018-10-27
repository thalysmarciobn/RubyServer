from ruby.communication.messages.Incoming import Incoming


class IMComputerInfo(Incoming):
    tokens = [28, 17]

    def dispatch(self, session, buffer_array):
        pass
