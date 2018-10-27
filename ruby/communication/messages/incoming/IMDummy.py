from ruby.communication.messages.Incoming import Incoming


class IMDummy(Incoming):
    tokens = [26, 26]

    def dispatch(self, session, buffer_array):
        pass
