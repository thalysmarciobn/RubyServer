from ruby.communication.messages.PacketManager import PacketManager
from ruby.network.SessionManager import SessionManager
from ruby.utils.Config import Config

configuration = Config().load()
session_manager = SessionManager()
packet_manager = PacketManager()