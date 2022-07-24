#1 - Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#'абвгдейка - это передача' = >" - это передача"

from WordsWork import GetFiltredWords

s = 'абвгдейка - это передача'
filter_ = 'абв'

print(GetFiltredWords(s, filter_))
