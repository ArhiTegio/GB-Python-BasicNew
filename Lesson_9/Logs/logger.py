from Lesson_9.Entities.LoggerStateMessage import LoggerStateMessage
from Lesson_9.Config.config import Config
import datetime

class Logger():

    @classmethod
    def write(cls, state: LoggerStateMessage, message: str):
        print(state.name, message)
        with open(Config.read()["logger_path"] + datetime.datetime.today().strftime('%Y-%m-%d') + '.log', "a") as file:
            file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {state.name} - {message}\n")
