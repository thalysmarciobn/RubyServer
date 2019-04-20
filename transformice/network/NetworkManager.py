import asyncore
import threading

from commons.communication.PacketManager import PacketManager
from commons.util import Logging
from transformice.messages.incoming.informations.INComputerInfo import INComputerInfo
from transformice.messages.incoming.informations.INCorrectVersion import INCorrectVersion
from transformice.messages.incoming.informations.INGameLog import INGameLog
from transformice.messages.incoming.player.INLanguage import INLanguage
from transformice.messages.incoming.server.INDummy import INDummy
from transformice.messages.incoming.server.INLogin import INLogin
from transformice.network.server.Network import Network


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
            NetworkManager.__loop_thread = threading.Thread(target=asyncore.loop, name="network")
            Logging.info("Network working on a dedicated thread")
            NetworkManager.__loop_thread.start()
            NetworkManager.__running = True

    @staticmethod
    def register():
        # Player
        PacketManager.register(INLanguage())
        # Information
        PacketManager.register(INCorrectVersion())
        PacketManager.register(INComputerInfo())
        PacketManager.register(INGameLog())
        # Server
        PacketManager.register(INLogin())
        PacketManager.register(INDummy())
        Logging.info(f"Packets loaded: {PacketManager.len()}")
