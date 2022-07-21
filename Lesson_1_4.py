#4-Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

from InputWork import GetValueCheck
from CoordinatWork import Position

print(f'Для четверти соответствуют слудующие возможные точки \n{Position(GetValueCheck("Введите четверть", True, lambda x: 1 <= x <= 4))}')