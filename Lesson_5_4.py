#4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

from ArchivingWork import Serialize, Deserialze

print("Исходный текст")
doc = "aaaaaaaaaabbbbbbbcccccbbbbddddccccccccccccdddddddddddgggggggggghhhhhjjjjjyyyjjjjuukkiiiiiiiiaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffffffffffffffffffffhhguyyyyyrrreeeeeeddddlllbbbbffffffffffffffffff,,,,,,,,,,,,,,,,,,,,,,,,,,,llll"
print(doc)

serial = Serialize(doc)
print("Сериализованный текст")
print(serial)

print("Десериализованный текст")
print(Deserialze(serial))
