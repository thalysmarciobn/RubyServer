from commons.communication.Output import Output


class OPImageLogin(Output):
    tokens = [100, 99]

    def __init__(self, image: str):
        super().__init__()
        self.bufferArray.writeUTF(image)
