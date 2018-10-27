from ruby.communication.messages.PacketManager import PacketManager
from ruby.database.DatabasePool import DatabasePool
from ruby.geoip.GeoIP import GeoIP
from ruby.network.SessionManager import SessionManager
from ruby.utils.Config import Config

configuration = Config().load()
geoip = GeoIP()
database = DatabasePool(configuration["Database"])
session_manager = SessionManager()
packet_manager = PacketManager()
