from functools import reduce
from MathWork import Divs


def GetFiltredWords(val:str, flter:str) -> str:
    splt = val.split(' ')
    arr = []
    cnt_filter = len(flter)
    for wrd in splt:
        cnt = 0
        for idx in range(len(wrd) - cnt_filter):
            if wrd[idx:idx+cnt_filter] == flter:
                cnt += 1
                break
        if cnt == 0:
            arr.append(wrd)

    return ' '.join(arr).strip()

def СlearDamagedLines(val:str) -> str:
    return ' '.join([e for e in val.split(' ') if len([c for c in e if str.isdigit(c)]) == 0])


def ScoreWords(arr):
    ar = []
    for idx, word in arr:
        val = score_word(idx, word)
        if val[2]:
            ar.append((val[0], val[1]))
    return ar

def score_word(idx, word):
    word = str.upper(word)
    sum_char = reduce(lambda x, y: x + y, [ord(c) for c in word])
    is_in_divs = sum_char in Divs(sum_char)
    return (word, sum_char if is_in_divs else idx, is_in_divs)