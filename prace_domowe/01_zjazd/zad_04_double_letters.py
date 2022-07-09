def double_letters(text: str):
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            return True
    return False


def test_double_letters_for_text_with_double_letters():
    assert double_letters("Hello") == True
    assert double_letters("pppppp") == True


def test_double_letters_for_text_without_double_letters():
    assert double_letters("abc") == False
    assert double_letters("nono") == False
    assert double_letters("ala") == False
    assert double_letters("") == False
