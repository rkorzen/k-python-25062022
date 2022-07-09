import pytest


def format_number(number: int) -> str:
    """Get positive numbers and return string representiation with comma separater thousands"""
    if number < 0:
        raise ValueError("Number should be positive")
    return f"{number:,}"


def test_format_number_correct():
    assert format_number(1000) == "1,000"
    assert format_number(0) == "0"
    assert format_number(1000000000) == "1,000,000,000"


def test_format_number_when_input_is_negative():
    with pytest.raises(ValueError):
        format_number(-1000)


def test_format_number_when_input_is_not_number():
    with pytest.raises(TypeError):
        format_number("ala ma kota")
