import asyncore
import threading

from bulle.messages.incoming.bulle.INBulle import INBulle
from bulle.messages.incoming.server.INDummy import INDummy
from bulle.network.server.Network import Network
from commons.communication.PacketManager import PacketManager


class NetworkManager:
    __running = False
    __loop_thread = None
    __networks = []

    @staticmethod
    def bind(host, port, backlog):
        network = Network(host=host, port=port, backlog=backlog)
        NetworkManager.__networks.append(network)

    @staticmethod
    def loop():
        if not NetworkManager.__running and NetworkManager.__loop_thread is None:
            NetworkManager.__loop_thread = threading.Thread(target=asyncore.loop(use_poll=True, map=None, count=None),
                                                            name="network")
            NetworkManager.__loop_thread.start()
            NetworkManager.__running = True

    @staticmethod
    def register():
        # Bulle
        PacketManager.register(INBulle())

        # Server
        PacketManager.register(INDummy())
