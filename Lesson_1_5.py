#5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#*Пример:*
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

from InputWork import GetValueCheck
from CoordinatWork import Point, Distence


print("Точка 1\n")
p1 = Point(GetValueCheck("Введите X:\n", True), GetValueCheck("Введите Y:\n", True))
print("Точка 2\n")
p2 = Point(GetValueCheck("Введите X:\n", True), GetValueCheck("Введите Y:\n", True))
print(Distence(p1, p2))
