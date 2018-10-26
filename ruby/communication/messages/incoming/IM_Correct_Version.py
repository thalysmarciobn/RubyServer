import random

from ruby import Controller
from ruby.communication.messages.Incoming import Incoming
from ruby.communication.messages.output.OP_Banner_Login import OP_Banner_Login
from ruby.communication.messages.output.OP_Correct_Version import OP_Correct_Version


class IM_Correct_Version(Incoming):

    tokens = [28, 1]

    def dispatch(self, Session, BufferArray):
        version = BufferArray.readShort()
        key = BufferArray.readUTF()
        if version == int(Controller.configuration["Transformice"]["Version"]) and key == str(Controller.configuration["Transformice"]["ConnectionKey"]):
            Session.send(OP_Correct_Version(Session.authKey, Session.lastPacketID))
            Session.send(OP_Banner_Login())
        else:
            pass
            #Session.disconnect()