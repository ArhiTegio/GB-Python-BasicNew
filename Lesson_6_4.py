#Задача: предложить улучшения кода для уже решённых задач:
#- С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce
#4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#Примеры
#список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#список: [], ищем: "123", ответ: -1


from WordsWork import SearchSecondStringInList


print(SearchSecondStringInList(["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"))
print(SearchSecondStringInList(["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу"))
print(SearchSecondStringInList(["йцу", "фыв", "ячс", "цук", "йцукен"], "йцу"))
print(SearchSecondStringInList(["123", "234", 123, "567"], "123"))
print(SearchSecondStringInList([], "123"))