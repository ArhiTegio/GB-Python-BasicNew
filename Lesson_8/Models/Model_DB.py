from Lesson_8.Models.Model_Json_Worker import Model_Json_Worker
from Lesson_8.Logs.logger import Logger, LoggerStateMessage
from Lesson_8.Entities.State import State
import sys

class Model_DB():
    @classmethod
    def Add(self, row):
        data = Model_Json_Worker.read_tasks()
        data.append(row)
        Model_Json_Worker.write_tasks(data)
        Logger.write(LoggerStateMessage.INFO, "Записана новая строка")
        return data


    @classmethod
    def Done(self, idx: int):
        data = Model_Json_Worker.read_tasks()
        data[idx]['3.state'] = State.Done.name
        Model_Json_Worker.write_tasks(data)
        Logger.write(LoggerStateMessage.INFO, "Выполнено задание")
        return data


    @classmethod
    def Update(self, idx: int, row):
        data = Model_Json_Worker.read_tasks()
        data[idx] = row
        Model_Json_Worker.write_tasks(data)
        Logger.write(LoggerStateMessage.INFO, "Обнавлено задание")
        return data


    @classmethod
    def ChangePriorety(self, idx: int, priority: int):
        data = Model_Json_Worker.read_tasks()
        if priority <= 1:
            data[idx]['4.priority'] = State.Preority_1.name
        elif priority == 2:
            data[idx]['4.priority'] = State.Preority_2.name
        elif priority == 3:
            data[idx]['4.priority'] = State.Preority_3.name
        elif priority == 4:
            data[idx]['4.priority'] = State.Preority_4.name
        elif priority >= 5:
            data[idx]['4.priority'] = State.Preority_5.name

        Model_Json_Worker.write_tasks(data)
        Logger.write(LoggerStateMessage.INFO, "Изменен приоритет")
        return data


    @classmethod
    def Delete(self, idx):
        data = Model_Json_Worker.read_tasks()
        data[idx]['3.state'] = State.Delete.name
        Model_Json_Worker.write_tasks(data)
        Logger.write(LoggerStateMessage.INFO, "Удвлена задача")
        return data


    @classmethod
    def ViewAllTasks(self):
        data = Model_Json_Worker.read_tasks()
        Logger.write(LoggerStateMessage.INFO, "Загружены все данные")
        return data


    @classmethod
    def Identification(self, log, pas):
        data = Model_Json_Worker.read_identity()
        identity = len([e for e in data if e['log'] == log and e['pas'] == pas]) > 0
        Logger.write(LoggerStateMessage.INFO, "Удачный вход" if identity else "Неудачный вход")
        return identity


    @classmethod
    def Exit(self):
        sys.exit()

