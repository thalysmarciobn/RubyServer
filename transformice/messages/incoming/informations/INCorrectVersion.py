import random

from commons.communication.Incoming import Incoming
from commons.communication.Rules import Rules
from transformice.messages.output.game.OPBannerLogin import OPBannerLogin
from transformice.messages.output.server.OPCorrectVersion import OPCorrectVersion
from transformice.messages.output.transformice.OPImageLogin import OPImageLogin
from transformice.game.ClientManager import ClientManager
from commons.geoip.GeoIP import GeoIP


class INCorrectVersion(Incoming):
    __version = 483
    __key = "JjfAhchpMiir"
    __banners = [20]
    __background = "x_noel2014.jpg"

    tokens = [28, 1]
    rule = Rules.session

    def dispatch(self, session, buffer_array):
        version = buffer_array.readShort()
        key = buffer_array.readUTF()
        if version == self.__version and key == self.__key:
            last_packet_id = random.randint(0, 99)
            session.last_packet_id = last_packet_id
            flag = GeoIP.get(session.ip_address).name
            session.send(OPCorrectVersion(ClientManager.len(), flag, last_packet_id, session.authKey, session.authKeyLogin))
            session.send(OPBannerLogin(self.__banners))
            session.send(OPImageLogin(self.__background))
        else:
            session.disconnect()