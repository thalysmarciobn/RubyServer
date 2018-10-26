from ruby.network.buffer.Encoder import Encoder


class Tests:

    def send(self, data):
        encoder = Encoder()
        message = encoder.encoder(data)
        print(message)
        pass