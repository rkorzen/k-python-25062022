def is_palindrome(text: str):
    signs = [x for x in text.lower() if x.isalnum()]
    return signs == signs[::-1]


def test_is_palindrome():
    assert is_palindrome("Kajak") is True
    assert is_palindrome("Kobyła ma mały bok!") is True
    assert is_palindrome("Alx") is False
