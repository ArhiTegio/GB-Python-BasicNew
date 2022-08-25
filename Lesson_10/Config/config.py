import json

class Config():
    path = './config.json'

    @classmethod
    def read(self):
        config = []
        with open(self.path, "r") as file:
                config = json.load(file)
        return config

    @classmethod
    def write(self, config):
        with open(self.path, "w") as file:
            file.write(json.dumps(config))

