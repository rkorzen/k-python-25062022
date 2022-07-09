def max_of_two(a, b):
    if a >= b:
        return a
    return b


def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))


def test_max_of_three():
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(1, 0, 0) == 1
