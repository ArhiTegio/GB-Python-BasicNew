def Serialize(doc:str):
    dic = {}
    dic_nearest = {}
    w = ''
    pos = 0
    max_pos = 0
    for idx, c in enumerate(doc):
        if w != c:
            if c in dic.keys():
                dic[c].append(idx)
            else:
                dic[c] = [idx]
            dic_nearest[pos] = idx
            w = c
            pos = idx
        max_pos = idx
    dic_nearest[pos] = max_pos

    arr = []
    for k, v in dic.items():
        v = [chr(i) for i in v]
        arr.append(f'{k} {" ".join(v)}>>')

    return ''.join([chr(max_pos), '>>'] + arr)


def Deserialze(doc:str):
    splt = doc.split(">>")
    if len(splt) == 0:
        return ''

    len_doc = ord(splt[0])+1
    arr = []
    for el in splt[1:]:
        splt_doc = el.split(' ')
        if len(splt_doc) > 1:
            k = splt_doc[0]
            for var in splt_doc[1:]:
                e = ord(var)
                arr.append((e, k))
    arr += [(len_doc, '')]
    arr.sort(key=lambda x: x[0])
    str_arr = []
    for idx in range(len(arr)-1):
        str = ''.join([arr[idx][1] for _ in range(arr[idx+1][0] - arr[idx][0])])
        str_arr.append(str)

    return ''.join(str_arr)

