from ruby import Controller
from ruby.Server import Server
from ruby.communication.messages.incoming.IM_Correct_Version import IM_Correct_Version
from ruby.utils import Logging

Controller.packet_manager.add(IM_Correct_Version())

Logging.info("Packets loaded: " + str(len(Controller.packet_manager)))

config = Controller.configuration

server = Server(config["Network"]["Address"], config["Network"]["Ports"], config["Network"]["Backlog"])
server.start()