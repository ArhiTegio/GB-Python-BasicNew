def GetValue(discription:str, is_digit:bool=False):
    while True:
        try:
            val = input(discription)
            if is_digit:
                val = int(''.join([ch for idx, ch in enumerate([c for c in val if str.isdigit(c) or c == '-']) if str.isdigit(ch) or idx == 0 and ch == '-']))
            break
        except Exception as ex:
            print(ex)
    return val


def GetValueCheck(description:str, is_digit:bool, lambda_=None):
    while True:
        val = GetValue(description, is_digit)
        if lambda_ is None or lambda_(val):
            break
    return val
