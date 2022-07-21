#1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#*Пример:*
#- 6782 -> 23
#- 0,56 -> 11

from InputWork import GetValue

print(sum([int(e) for e in str(GetValue("Введите число:\n", True)) if str.isdigit(e)]))