from commons.network.buffer.BufferArray import BufferArray


class Output:
    tokens = []
    bufferArray = None

    def __init__(self):
        self.bufferArray = BufferArray()
