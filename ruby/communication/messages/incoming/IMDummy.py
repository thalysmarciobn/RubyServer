from ruby.communication.messages.Incoming import Incoming


class IMDummy(Incoming):
    tokens = [1, 1]

    def dispatch(self, session, buffer_array):
        pass
