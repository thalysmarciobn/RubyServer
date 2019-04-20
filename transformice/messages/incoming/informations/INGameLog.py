from commons.communication.Incoming import Incoming
from commons.communication.Rules import Rules
from commons.util import Logging


class INGameLog(Incoming):
    tokens = [28, 4]
    rule = Rules.sessionAndClient

    def dispatch(self, session, buffer_array):
        error_code1 = buffer_array.readByte()
        error_code2 = buffer_array.readByte()
        old_code1 = buffer_array.readByte()
        old_code2 = buffer_array.readByte()
        error = buffer_array.readUTF()
        if error_code1 == 1 and error_code2 == 1:
            Logging.packet("OLD", f"GameLog [{old_code1}, {old_code2}] error: " + str(error))
        elif error_code1 == 60 and error_code2 == 3:
            Logging.packet("TRIBULLE", f"GameLog {old_code1}] error: " + str(error))
        else:
            Logging.packet("PROTOCOL", f"GameLog [{error_code1}, {error_code2}] error: " + str(error))


