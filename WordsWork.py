from functools import reduce
from MathWork import Divs
from typing import List, Union


def GetFiltredWords(val: str, flter: str) -> str:
    '''
    Получить
    :param val:
    :param flter:
    :return:
    '''
    splt = val.split(' ')
    arr = []
    cnt_filter = len(flter)
    for wrd in splt:
        cnt = 0
        for idx in range(len(wrd) - cnt_filter):
            if wrd[idx:idx + cnt_filter] == flter:
                cnt += 1
                break
        if cnt == 0:
            arr.append(wrd)

    return ' '.join(arr).strip()


def СlearDamagedLines(val: str) -> str:
    '''
    Отфильтровать из предложения строки с добавленными числами
    :param val: Предложение
    :return: Очищенное предложение
    '''
    return ' '.join([e for e in val.split(' ') if len([c for c in e if str.isdigit(c)]) == 0])


def IsStringInDocument(doc: List[str], vals: Union[str, int, float]) -> bool:
    '''
    Определить, присутствует ли в заданном списке строк, некоторое число
    :param doc: Лист строк из докуметна
    :param vals: Проверяемы строки и числа
    :return: Найдены ли проверяемые строки в списке строк
    '''
    cnt = 0
    for val in vals:
        val = str(val)
        cnt += len(list(filter(lambda x: val in x, doc)))
    return True if cnt > 0 else False


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


def SearchSecondStringInList(docs: List[Union[str, int]], val: str) -> int:
    '''
    Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
    :param docs: Список слов
    :param val: проверяемое слово
    :return: возвращает позицию или -1 если такого слова нет во втором вхождении
    '''
    lst = list(filter(lambda x: x[1] == val, enumerate(docs)))
    if len(lst) >= 2:
        return int(lst[1][0])
    else:
        return -1
