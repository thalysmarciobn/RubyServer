import time


class Time:

    @staticmethod
    def get():
        return int(str(time.time())[:10])