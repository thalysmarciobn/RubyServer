import asyncore

from ruby.network.Network import Network
from ruby.utils import Logging


class Server:

    def __init__(self, host, ports, backlog):
        self.__host = host
        self.__ports = ports
        self.__backlog = backlog
        self.__validPorts = []

    def start(self):
        Logging.info("Starting server.")
        for port in self.__ports:
            try:
                Network(self.__host, port, self.__backlog)
                self.__validPorts.append(port)
            except Exception as e:
                Logging.alert(f"Can't bind on port: {port}")
        Logging.info(f"Server working on ports: {self.__validPorts}")
        asyncore.loop(timeout=30.0, use_poll=False, map=None, count=None)
