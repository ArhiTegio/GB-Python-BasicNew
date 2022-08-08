from sys import platform
from Lesson_8.Entities.Row import Database
from Lesson_8.Controllers.Subscribtion import Controller_Task
import os


class View():
    def __init__(self):
        self.log = ''
        self.pas = ''
        self.view = 0
        self.controller = Controller_Task()
        self.data = []


    def Show(self):
        while True:
            if self.view == 0:
                self.ViewInden()
            if self.view == 1:
                self.ViewMain()


    def ViewMain(self):
        lst = [func for func in dir(Controller_Task) if callable(getattr(Controller_Task, func)) and '__' not in func and 'Ident' not in func and 'Exit' not in func]
        lst.append('Exit')

        self.Clear()
        print('Данные. ')
        for idx, row in enumerate(self.data):
            print(f'{idx}. {row}')

        print()
        print('Список действий: ')
        for idx, el in enumerate(lst):
            print(f'{idx}. {el}')
        print()

        print('Введите номер действия: ')
        ipt = ''.join([ e for e in input("") if str.isdigit(e)])
        if len(ipt) > 0:
            ipt = int(ipt)
            if ipt < len(lst):
                st = lst[ipt]
                if st == 'Exit':
                    self.view = 0
                    self.controller.Exit()
                elif st == 'Add':
                    row_new = Database.GetNewRowDatabase()
                    row_new['log'] = self.log
                    print('Создается новая строка: ')
                    print(row_new)
                    row_new = self.UpdateRow(row_new)
                    self.data = self.controller.Add(row_new)
                    self.data = self.controller.ViewAllTask()
                elif st == 'Done':
                    if len(self.data) > 0:
                        row = self.GetRow()
                        self.controller.Done(row)
                        self.data = self.controller.ViewAllTask()
                    else:
                        print('Нет данных')
                elif st == 'Delete':
                    if len(self.data) > 0:
                        row = self.GetRow()
                        self.controller.Delete(row)
                        self.data = self.controller.ViewAllTask()
                    else:
                        print('Нет данных')
                elif st == 'Update':
                    if len(self.data) > 0:
                        idx = self.GetRow()
                        row = self.data[idx]
                        row = self.UpdateRow(row)
                        self.controller.Update(idx, row)
                        self.data = self.controller.ViewAllTask()
                    else:
                        print('Нет данных')
                elif st == 'ChangePriorety':
                    if len(self.data) > 0:
                        idx = self.GetRow()
                        priority = self.GetPriority()
                        self.controller.ChangePriorety(idx, priority)
                        self.data = self.controller.ViewAllTask()
                    else:
                        print('Нет данных')
                elif st == 'ViewAllTask':
                    self.data = self.controller.ViewAllTask()


    def GetRow(self):
        while True:
            print('Введите индекс строки: ')
            ipt = ''.join([e for e in input("") if str.isdigit(e)])
            if len(ipt) > 0:
                ipt = int(ipt)
                if ipt < len(self.data):
                    break
        return ipt

    def GetPriority(self):
        while True:
            print('Введите приоритет (1 - 5) строки: ')
            ipt = input("")
            ipt = ''.join([e for e in ipt if str.isdigit(e)])
            if len(ipt) > 0:
                ipt = int(ipt)
                if 0 <= ipt <= 5:
                    break
        return ipt


    def UpdateRow(self, row):
        while True:
            print('Введите параметры с номером позиции через пробел для изменения:  (пример: 1.Новая задача 2.Нужно_выполнить)')
            pr = input("").strip().replace('  ', ' ').split(' ')
            lst_key = list(row.keys())
            for call in pr:
                element = list(call.split('.'))
                element[0] = ''.join([e for e in element[0] if str.isdigit(e)])
                if len(element) == 2 and len(element[0]) > 0:
                    idx = int(element[0])
                    val = element[1]
                    if idx < len(row):
                        row[lst_key[idx]] = val
            print(f'Обновленная строка имеет следующий вид:')
            print(f'{row}')
            print("")
            print("Введено все верно? Д/н")
            ipt = input("")
            if 'д' in str.lower(ipt):
                break

        return row


    def ViewInden(self):
        self.Clear()
        print('Введите логин и пароль через пробел: ')
        lst = input(" ").replace('  ', ' ').strip().split(' ')
        if len(lst) > 1 and self.controller.Identification(log=lst[0], pas=lst[1]):
            self.log = lst[0]
            self.view = 1
            self.data = self.controller.ViewAllTask()
        else:
            self.view = 0


    def Clear(self):
        xs = ''
        if platform in ["linux", "linux2", 'osx', 'posix', "darwin"]:
            xs = 'clear'
        elif platform in ["win32", 'nt', 'dos']:
            xs = 'cls'
        clear = lambda:os.system(xs)
        clear()






