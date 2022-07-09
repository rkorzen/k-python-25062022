def flatten(input: list) -> list:
    output = []

    for el in input:
        if not isinstance(el, list):
            output.append(el)
        else:
            for e in flatten(el):
                output.append(e)
    return output


def test_flatten():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten([[1, 2], [3, 4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]
