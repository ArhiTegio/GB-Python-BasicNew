#4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
#не использовать random.randint и вообще библиотеку random
#Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

import time
import gc


arr = []
for e in range(10):
    start = time.process_time()
    gc.collect()
    v = time.process_time() - start
    val = str(time.process_time() - start)
    val_ = []
    for e in val:
        if e in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            val_.append(e)
        if len(val_) > 3:
            break
    p1, p2 = int(val[-2:][0]), int(val[-4:-2][1])
    val_ = int(str(''.join(val_)))
    val_ <<= p1
    val_ ^= p2
    v_ = v * val_
    while True:
        if int(v_) == 0:
            break
        v_ /= 10
    arr.append(v_)
print(arr)