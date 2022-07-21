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
        yield arr[1] * -1
        for idx, _ in enumerate(range(val-1)):
            tmp = arr[0] + arr[1]
            arr[0], arr[1] = arr[1], tmp
            yield tmp  if idx % 2 == 0 else tmp * -1


def TwoDirectionalFibbonachi(val:int):
    positive = [e for e in fibbonach(val)]
    negative = [e for e in fibbonach_neg(val)][1:]
    negative.reverse()
    negative.extend(positive)

    return negative



def SumRamandgan(epoch_k:int):
    return sum([(factorial(4*k)/(factorial(k)**4))*abs(1103+26390*k)/((4*99)**(4*k)) for k in range(epoch_k)])


def factorial(n:int) -> int:
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


def get_count(val:float):
    s = str(val)
    pos = position_delimiter(s)
    return len(s[pos+1:])


def position_delimiter(val:str) -> int:
    pos = 0
    for pos in range(len(val)):
        if val[pos] in [',', '.']:
            break
    return pos


def Pi(round:float = 0.000000000000001) -> float:
    val = 9801 / (2 * (2 ** 0.5) * SumRamandgan(3))
    s = str(val)
    pos = position_delimiter(s)
    return float(s[:pos+get_count(round)+1])


def GetNonDoubleNum(arr):
    d1 = {}
    d2 = {}
    for el in arr:
        if el in d1.keys():
            d2[el] = 1
            d1.pop(el)
        elif el not in d2.keys():
            d1[el] = 1
        else:
            d2[el] += 1
    return list(d1.keys())

def GetMultipliers(N:int):
    r = 0
    min_ = 100000
    for i in range(1+1, N-1):
        val = N % i
        if val == 1:
            r = i
            break

        elif min_ > val:
            r = i
            min_ = val

    return [r, round(N / r, 15)]


def GetMulti(N:int):
    return [e for e in range(1+1, N) if N % e == 0]