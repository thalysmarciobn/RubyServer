from database.DatabasePool import DatabasePool
from ruby.communication.messages.PacketManager import PacketManager
from ruby.network.SessionManager import SessionManager
from ruby.utils.Config import Config

configuration = Config().load()
database = DatabasePool(configuration["Database"])
session_manager = SessionManager()
packet_manager = PacketManager()
