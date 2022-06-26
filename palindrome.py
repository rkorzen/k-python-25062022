def is_palindrom(text: str) -> bool:
    tmp = ""
    for sign in text.lower():
        if sign.isalnum():
            tmp += sign
    #     if tmp == tmp[::-1]
    #         return True
    #     else:
    #         return False

    return tmp == tmp[::-1]


def xxx(a: int):
    return a**2


assert is_palindrom("kajak") is True
assert is_palindrom("Kobyła ma mały bok!") is True
assert is_palindrom("dom") is False
