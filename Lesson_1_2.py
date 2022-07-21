# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from InputWork import GetValue
import BackLogic as bl

vals = {e: bool(GetValue(f"Введите значение  {e}:\n")) for e in ['X', 'Y', 'Z']}
print(f"¬({vals['X']} ⋁ {vals['Y']} ⋁ {vals['Z']}) = ¬{vals['X']} ⋀ ¬{vals['Y']} ⋀ ¬{vals['Z']} = {bl.funcs['Урок 1 задане 2']['lambda'](vals['X'], vals['Y'], vals['Z'])}")
