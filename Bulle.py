import time

from bulle.manager.BulleManager import BulleManager
from bulle.network.NetworkManager import NetworkManager
from bulle.rpc.RpcManager import RpcManager
from commons.database.DatabasePool import DatabasePool
from commons.geoip.GeoIP import GeoIP
from commons.util import Logging


class Bulle:
    __valid_ports = []
    __host = "127.0.0.1"
    __backlog = 100
    __ports = [443, 5555, 4112, 6112, 44444, 44440, 3724]

    __packet_keys = [16, 49, 58, 28, 54, 60, 8, 17, 47, 10, 105, 115, 72, 105, 98, 68, 110, 100, 96, 121]
    __identification_keys = [6437417, 1024, 8192, 7217557, 676121, 2097152, 268435456, 8083262, 16, 6284744]

    __geo_ip = "resources/geoip/GeoLite2-Country.db"

    __mysql_host = "127.0.0.1"
    __mysql_port = 3306
    __mysql_user = "root"
    __mysql_pass = "123456"
    __mysql_data = "transformice"
    __mysql_pool = 5
    __mysql_reset = True

    def __init__(self):
        Logging.info("Starting server.")
        self.__start = int(round(time.time() * 1000))
        GeoIP.build(self.__geo_ip)
        NetworkManager.register()
        if DatabasePool.connect(
                pool_name=self.__mysql_data,
                pool_size=self.__mysql_pool,
                pool_reset_session=self.__mysql_reset,
                database=dict(
                    host=self.__mysql_host,
                    port=self.__mysql_port,
                    user=self.__mysql_user,
                    password=self.__mysql_pass,
                    database=self.__mysql_data
                )
        ):
            RpcManager.connect()
            for port in self.__ports:
                try:
                    NetworkManager.bind(host=self.__host, port=port, backlog=self.__backlog)
                    self.__valid_ports.append(port)
                except OSError as error:
                    Logging.alert(f"Can't bind on port: {port}, {error}")
            if len(self.__valid_ports) > 0:
                Logging.info(f"Server working on ports: {self.__valid_ports}")
                Logging.info(f"Server started in {int(round(time.time() * 1000)) - self.__start}ms")
                BulleManager.build()
                NetworkManager.loop()


if __name__ == "__main__":
    bulle = Bulle()
