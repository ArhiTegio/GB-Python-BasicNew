#4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#*Пример:*
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

from MathWork import DecimalToDischarge

for el in [45, 3, 2]:
    print(f'{el} -> {DecimalToDischarge(el)}')

