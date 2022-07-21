from typing import List, Union


def GetSequence(val:int):
    arr = []
    v = 1
    for e in range(1, val+1):
        v = e * v
        arr.append(v)
    return arr


def GetSequence2(val:int):
    return {n: (1 + 1 / n) ** n for n in range(1, val + 1)}


Nums_types = Union[int,float]


def SumNonevenSequennce(arr:List[Nums_types]) -> int:
    sum_elements = 0
    for idx in range(1, len(arr), 2):
        sum_elements += arr[idx]
    return sum_elements


def ProductPairsNumbers(arr:List[Nums_types]) -> List[Nums_types]:
    sum_par_elements = []
    len_arr = len(arr)
    for idx in range(int(len_arr / 2)):
        sum_par_elements.append(arr[idx] * arr[len_arr - idx - 1])
    if len_arr / 2.0 > int(round(len_arr / 2, 2)):
        el = arr[int(len_arr / 2)]
        sum_par_elements.append(el*el)
    return sum_par_elements


def DiffMinMaxFractionalPart(arr:List[Nums_types]):
    min_sq = 1.
    max_sq = 0.

    for idx in range(len(arr)):
        fractional_part = round(float(arr[idx]) - float(int(arr[idx])), 15)

        if fractional_part > max_sq:
            max_sq = fractional_part
        if fractional_part < min_sq:
            min_sq = fractional_part

    return {"Diff": max_sq - min_sq, 'MinFractional': min_sq, 'MaxFractional': max_sq}


def DecimalToDischarge(val:int, dis:int=2):
    arr = []
    while True:
        pos = int(val / dis) * dis
        arr.append(val - pos)
        val = int(pos / dis)
        if val <= 1:
            arr.append(val)
            break
    arr.reverse()
    return int(''.join([str(e) for e in arr]))


def fibbonach(val:int):
    arr = [0, 1]
    yield arr[0]
    if val > 0:
        yield arr[1]
        for _ in range(val-1):
            tmp = arr[0] + arr[1]
            arr[0], arr[1] = arr[1], tmp
            yield tmp


def fibbonach_neg(val:int):
    arr = [0, -1]
    yield arr[0]
    if val > 0:
        yield arr[1]
        for _ in range(val-1):
            tmp = arr[0] + arr[1]
            arr[0], arr[1] = arr[1], tmp
            yield tmp


def TwoDirectionalFibbonachi(val:int):
    positive = [e for e in fibbonach(val)]
    negative = [e for e in fibbonach_neg(val)][1:]
    negative.reverse()
    negative.extend(positive)

    return negative







