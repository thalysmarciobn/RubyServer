import sys

from bulle.game.clients.Client import Client
from commons.util import Logging


class ClientManager:
    __clients = {}
    __clients_code = {}
    __last_player_code = 0

    @staticmethod
    def append(session, data):
        name = data.get("Username")
        if name not in ClientManager.__clients:
            player_code = ClientManager.generateCode()
            client = Client(session, data, player_code)
            session.setClient(client)
            ClientManager.__clients.update({name: client})
            ClientManager.__clients_code.update({player_code: client})
            Logging.info(f"[{name}] client has been connected.")
            return client
        return None

    @staticmethod
    def remove(client):
        name = client.data().get("Username")
        if name in ClientManager.__clients:
            ClientManager.__clients.pop(name)
            ClientManager.__clients_code.pop(client.playerCode())
            Logging.info(f"[{name}] has been disconnected.")

    @staticmethod
    def len():
        return len(ClientManager.__clients)

    @staticmethod
    def contains(username: str):
        return username in ClientManager.__clients

    @staticmethod
    def generateCode():
        ClientManager.__last_player_code += 1 % sys.maxsize
        return ClientManager.__last_player_code