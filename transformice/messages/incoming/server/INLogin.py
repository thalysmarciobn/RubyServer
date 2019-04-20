from commons.communication.Incoming import Incoming
from commons.communication.Rules import Rules
from commons.database.DatabasePool import DatabasePool
from commons.util.Time import Time
from transformice.game.ClientManager import ClientManager
from controller.game.RoomManager import RoomManager
from transformice.messages.output.informations.OPTime import OPTime
from transformice.messages.output.player.OPShamanExp import OPShamanExp
from transformice.messages.output.player.OPShamanSkills import OPShamanSkills
from transformice.messages.output.server.OPLoginResult import OPLoginResult
from transformice.messages.output.server.OPPlayerIdentification import OPPlayerIdentification
from transformice.messages.output.shop.OPShamanItems import OPShamanItems
from transformice.messages.output.tribulle.OPNewTribulle import OPNewTribulle
from transformice.rpc.RpcManager import RpcManager


class INLogin(Incoming):
    tokens = [26, 8]
    rule = Rules.session

    def dispatch(self, session, buffer_array):
        packet = buffer_array
        username = packet.readUTF()
        password = packet.readUTF()
        url = packet.readUTF()
        start_room = packet.readUTF()
        result_key = packet.readInt()
        packet.readByte()
        packet.readUTF()
        #    session.disconnect()
        #    return
        if ClientManager.contains(username):
            session.send(OPLoginResult(1, ""))
            return
        data = DatabasePool.execute("select * from users WHERE Username = %(username)s and password = %(password)s",
                                    {"username": username, "password": password})
        if data is None:
            session.send(OPLoginResult(2, ""))
            return
        client = ClientManager.append(session, data)
        session.client = client
        client.send(OPTime(Time.get()))
        client.send(OPShamanSkills([], False))
        client.send(OPShamanExp(0, 0, 32))
        language = session.language
        client.send(
            OPPlayerIdentification(data.get("ID"), data.get("Username"), data.get("Time"), language.value,
                                   client.isGuest(), client.playerCode(), data.get("PrivLevel"), data.get("LuaDev"),
                                   data.get("MapCrew"),
                                   data.get("FunCorp"), data.get("FashionSquad")))

        client.send(OPShamanItems([], []))
        client.send(OPNewTribulle(True))
        RpcManager.enterRoom(language.name.lower(), client.playerCode(), start_room)
        # identification = data.readUTF()
        # print(identification)
