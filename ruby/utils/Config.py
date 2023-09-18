import json


class Config:
    @staticmethod
    def load():
        with open("configuration.json", "r") as read_file:
            data = json.load(read_file)
        return data
