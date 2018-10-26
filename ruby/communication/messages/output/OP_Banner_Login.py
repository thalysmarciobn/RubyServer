from ruby import Controller
from ruby.communication.messages.Output import Output

class OP_Banner_Login(Output):

    output = [16, 9]

    def __init__(self):
        self.bufferArray.writeShort(Controller.configuration["Transformice"]["Banner"])
        self.bufferArray.writeByte(1)
        self.bufferArray.writeBool(True)
        self.bufferArray.writeBool(False)