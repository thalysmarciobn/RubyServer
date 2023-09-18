from ruby import Controller
from ruby.communication.messages.Output import Output


class OPDummy(Output):
    output = [1, 1]

    def __init__(self):
        self.bufferArray.writeBool(True)
