#1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#*Пример:*
#- 6 -> да
#- 7 -> да
#- 1 -> нет

from DateTimeWork import DataTimest
from InputWork import GetValue

day_num = GetValue("Введите день недели\n", True) - 1
dt = DataTimest()
answer = dt[day_num]
print(f'День недели {answer["name"]} является {"выходным" if answer["is_weekend"] else "будним"}')

