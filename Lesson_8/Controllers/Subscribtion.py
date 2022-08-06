from Lesson_8.Models.Model_DB import Model_DB


class Controller_Task():
    def Add(self, row):
        return Model_DB.Add(row)

    def Done(self, idx: int):
        return Model_DB.Done(idx)

    def ViewAllTask(self):
        return Model_DB.ViewAllTasks()

    def Update(self, idx: int, row):
        return Model_DB.Update(idx, row)

    def Delete(self, idx:int):
        return Model_DB.Delete(idx)

    def Identification(self, log, pas):
        return Model_DB.Identification(log, pas)

    def ChangePriorety(self, idx: int, priority: int):
        return Model_DB.ChangePriorety(idx, priority)

    def Exit(self):
        Model_DB.Exit()

