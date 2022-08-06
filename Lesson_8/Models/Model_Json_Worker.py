from Lesson_8.Config.config import Config
import json


class Model_Json_Worker():
    @classmethod
    def read_tasks(cls):
        data = []
        with open(Config.read()['db_data'], "r") as file:
            for line in file:
                data.append(json.loads(line))
        return data


    @classmethod
    def write_tasks(cls, data):
        with open(Config.read()['db_data'], "w") as file:
            for d in data:
                file.write(json.dumps(d))


    @classmethod
    def read_identity(cls):
        data = []
        with open(Config.read()['db_identity'], "r") as file:
            for line in file:
                data.append(json.loads(line))
        return data


    @classmethod
    def write_identity(cls, data):
        with open(Config.read()['db_identity'], "w") as file:
            for d in data:
                file.write(json.dumps(d))

