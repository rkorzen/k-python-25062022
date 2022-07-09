import pytest


def sumator(elements):
    if hasattr(elements, "values"):
        elements = elements.values()

    result = 0

    for el in elements:
        try:
            result += int(el)
        except ValueError:
            pass
    return result


def test_sumator_list_tuple_set():
    assert sumator([1, 2, 3]) == 6
    assert sumator(["10", 20, "30"]) == 60
    assert sumator(["-10", -20, "-30"]) == -60
    assert sumator((1, 2, 3)) == 6
    assert sumator({11, 2, 3}) == 16


@pytest.mark.parametrize(
    "input,expected",
    [
        ([1, 2, 3], 6),
        (["10", 20, "30"], 60),
        (["-10", -20, "-30"], -60),
        ((1, 2, 3), 6),
        ({11, 2, 3}, 16),
    ],
)
def test_sumator_list_tuple_set(input, expected):
    assert sumator(input) == expected


def test_sumator_dict():
    data = {"a": 10, "b": 20, "c": 100}
    assert sumator(data) == 130


def test_sumator_not_iterable():
    with pytest.raises(TypeError):
        sumator(1111)
