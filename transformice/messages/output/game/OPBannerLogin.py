from commons.communication.Output import Output


class OPBannerLogin(Output):
    tokens = [16, 9]

    def __init__(self, banners: list):
        super().__init__()
        self.bufferArray.writeByte(len(banners))
        for banner in banners:
            self.bufferArray.writeByte(banner)
        self.bufferArray.writeBool(True)
        self.bufferArray.writeBool(False)
