#Задана натуральная степень n. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать
#в файл многочлен степени n.
#*Пример: n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
from MathWork import GetDegree


n = 10
arr = f"{' * '.join(list(filter(lambda x: x != '', [GetDegree(random.randint(1, 100), n)] + [GetDegree(random.randint(0, 100), idx) for e, idx in enumerate(range(n-1, -1, -1))])))} = 0"
print(arr)
