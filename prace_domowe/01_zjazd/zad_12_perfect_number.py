def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


def test_perfect_number():
    assert perfect_number(6) == True
    assert perfect_number(28) == True
    assert perfect_number(496) == True
    assert perfect_number(8128) == True
    assert perfect_number(8121) == False
