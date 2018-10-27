import random

from ruby import Controller
from ruby.communication.messages.Incoming import Incoming
from ruby.communication.messages.output.OPBannerLogin import OPBannerLogin
from ruby.communication.messages.output.OPCorrectVersion import OPCorrectVersion


class IMCorrectVersion(Incoming):

    tokens = [28, 1]

    def dispatch(self, session, buffer_array):
        version = buffer_array.readShort()
        key = buffer_array.readUTF()
        if version == int(Controller.configuration["Transformice"]["Version"]) and key == str(Controller.configuration["Transformice"]["ConnectionKey"]):
            session.lastPacketID = random.randrange(0, 99)
            session.send(OPCorrectVersion(session.ipAddress, session.authKey, session.lastPacketID))
            session.send(OPBannerLogin())
        else:
            session.disconnect()