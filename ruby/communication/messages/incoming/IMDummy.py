from ruby.communication.messages.Incoming import Incoming
from ruby.communication.messages.output.OPDummy import OPDummy


class IMDummy(Incoming):
    tokens = [1, 1]

    def dispatch(self, session, buffer_array):
        session.send(OPDummy())
