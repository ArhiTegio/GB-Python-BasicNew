#Задача: предложить улучшения кода для уже решённых задач:
#- С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce

#1- Определить, присутствует ли в заданном списке строк, некоторое число

from typing import List, Union
from WordsWork import IsStringInDocument


doc = ['123dsd', 'ddd', '689,344d']
print(IsStringInDocument(doc, [68, 'mm']))
print(IsStringInDocument(doc, [7.6]))
