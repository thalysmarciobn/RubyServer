from ruby.Server import Server
from ruby.utils import Logging
from ruby import Controller

def main():
    Logging.info("Packets loaded: " + str(len(Controller.packet_manager)))


    config = Controller.configuration

    server = Server(config["Network"]["Address"], config["Network"]["Ports"], config["Network"]["Backlog"])
    server.start()

if __name__ == "__main__":
    main()