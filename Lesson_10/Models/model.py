import json


class Model():
    @classmethod
    def read(cls, link):
        data = []
        with open(link, "r") as file:
            for line in file:
                data.append(json.loads(line))
        return data

    @classmethod
    def write(cls, data, link):
        with open(link, "w") as file:
            for d in data:
                file.write(json.dumps(d) + '\n')