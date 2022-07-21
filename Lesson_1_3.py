#3- Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

from InputWork import GetValueCheck
from CoordinatWork import Point


x = GetValueCheck("Введите X:\n", True, lambda x: x != 0)
y = GetValueCheck("Введите Y:\n", True, lambda y: y != 0)
point = Point(x, y)
print(point.PointPosition())
