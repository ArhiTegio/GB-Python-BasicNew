#2- Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности. Посмотрели, что такое множество? Вот здесь его не используйте.

from MathWork import GetNonDoubleNum

s = set()

assert GetNonDoubleNum([]) == [], "Что то не так"
assert GetNonDoubleNum([1, '2', '3', '2', 1]) == ['3'], 'Что то не так'

print(GetNonDoubleNum([1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 34, 4, 5, 6, 6, 8]))
