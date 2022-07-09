import pytest


def mid(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("Input should be a string")
    length = len(text)
    if length % 2 == 0:
        return ""
    return text[length // 2]


def test_mid_for_text_with_middle_letter():
    assert mid("abc") == "b"
    assert mid("pythonistas") == "n"
    assert mid("b") == "b"


def test_mid_for_empty_str():
    assert mid("") == ""


def test_mid_for_text_without_middle_letter():
    assert mid("abbc") == ""
    assert mid("python") == ""


def test_mid_for_non_str_input():
    with pytest.raises(ValueError):
        mid([1, 2, 3])
