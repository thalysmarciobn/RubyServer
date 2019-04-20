from commons.communication.Incoming import Incoming
from commons.communication.Rules import Rules


class INComputerInfo(Incoming):
    tokens = [28, 17]
    rule = Rules.session

    def dispatch(self, session, buffer_array):
        pass
