#2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#*Пример:*
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from InputWork import GetValueCheck
from MathWork import GetSequence




val = GetValueCheck("Введте число:\n", True, lambda x: x > 0)

print(GetSequence(val))
