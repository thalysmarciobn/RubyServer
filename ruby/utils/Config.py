import json

class Config:
    def load(self):
        with open("configuration.json", "r") as read_file:
            data = json.load(read_file)
        return data