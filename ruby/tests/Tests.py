from ruby.network.buffer.Encoder import Encoder


class Tests:

    @staticmethod
    def send(data):
        encoder = Encoder()
        message = encoder.encoder(data)
        print(message)
        pass