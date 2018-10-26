from ruby.Server import Server
from ruby import Controller


def main():
    config = Controller.configuration
    if Controller.database.connect():
        server = Server(config["Network"]["Address"], config["Network"]["Ports"], config["Network"]["Backlog"])

        print(Controller.database.execute("select * from users WHERE Username = %(username)s", {"username": "Thalys"}))
        server.start()


if __name__ == "__main__":
    main()
