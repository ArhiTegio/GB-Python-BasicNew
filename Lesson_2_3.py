#3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
#*Пример:*
#- Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

from InputWork import GetValueCheck
from MathWork import GetSequence2

val = GetValueCheck("Введите число:\n", True, lambda x: x > 0)

print(GetSequence2(val))

