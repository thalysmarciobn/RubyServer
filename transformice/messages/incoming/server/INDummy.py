from commons.communication.Incoming import Incoming
from commons.communication.Rules import Rules


class INDummy(Incoming):
    tokens = [26, 26]
    rule = Rules.sessionAndClient

    def dispatch(self, session, buffer_array):
        pass
