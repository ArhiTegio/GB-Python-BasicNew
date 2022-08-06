#Доделать решение задачи: Задача: Создать список дел.
#Работа также по командам.
#Функционал смотрите из реального приложения списка дел: добавление, отметка выполненным, редактирование, удаление, просмотр всех дел.
#Не забывайте про блок-схему проекта.

from Config.config import Config
from Lesson_8.Views.View import View


if __name__ == '__main__':
    view = View()
    view.Show()
    config = Config.read()
    config = {
        "core_client": [{'host': '127.0.0.1', 'port': '*'}],
        "db_data": "./DataBase/data.json",
        "db_identity": "./DataBase/identity.json",
        "logger_path": './Logs/',
    }
    Config.write(config)


