import asyncore
import socket

from ruby.network.sessions.Session import Session


class Network(asyncore.dispatcher):

    def __init__(self, host, port, backlog):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(backlog)

    def handle_accepted(self, client, address):
        Session(client, address)
