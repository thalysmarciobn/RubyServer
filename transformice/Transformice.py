from transformice.game.ClientManager import ClientManager
from transformice.game.clients.Client import Client
from transformice.messages.output.server.OPLoginResult import OPLoginResult


class Transformice:

    @staticmethod
    def login(session, data, start_room):
        print(data)
        if ClientManager.contains(data):
            session.send(OPLoginResult(1, ""))
            return
        if len(data) <= 0:
            session.send(OPLoginResult(2, ""))
            return
        client = Client(session, data[0], ClientManager.generatePlayerCode())
        ClientManager.append(client.data()["Username"], client)
        session.client = client