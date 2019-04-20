import asyncore
import socket

from transformice.network.sessions.Session import Session


class Network(asyncore.dispatcher):

    def __init__(self, host: str, port: int, backlog: int):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(backlog)

    def handle_accepted(self, client: socket, address: object):
        Session(client, address)