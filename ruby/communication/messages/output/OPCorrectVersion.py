from ruby import Controller
from ruby.communication.messages.Output import Output


class OPCorrectVersion(Output):
    output = [26, 3]

    def __init__(self, address, auth_key, last_packet_id):
        flag = Controller.geoip.get(address).name
        self.bufferArray.writeInt(0)  # players online
        self.bufferArray.writeByte(last_packet_id)
        self.bufferArray.writeUTF(flag.lower())
        self.bufferArray.writeUTF(flag.lower())
        self.bufferArray.writeInt(auth_key)
