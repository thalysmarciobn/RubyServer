from ruby.communication.messages.Incoming import Incoming
from ruby.utils import Logging


class IM_Game_Log(Incoming):
    tokens = [28, 4]

    def dispatch(self, Session, BufferArray):
        errorCode1 = BufferArray.readByte()
        errorCode2 = BufferArray.readByte()
        oldCode1 = BufferArray.readByte()
        oldCode2 = BufferArray.readByte()
        error = BufferArray.readUTF()
        if errorCode1 == 1 and errorCode2 == 1:
            Logging.packet("OLD", "GameLog Error C: " + str(oldCode1) + ", CC: " + str(oldCode2) + ", error: " + str(error))
        elif errorCode1 == 60 and errorCode2 == 3:
            Logging.packet("TRIBULLE", "GameLog Error Code: " + str(oldCode1) + ", error: " + str(error))
        else:
            Logging.packet("PROTOCOL", "GameLog Error C: " + str(errorCode1) + ", CC: " + str(errorCode2) + ", error: " + str(error))


