def pascal_triangle(n):
    row = [1]
    rows = [row]
    for i in range(n - 1):
        # print(lista)
        new_row = []
        new_row.append(row[0])
        for i in range(len(row) - 1):
            new_row.append(row[i] + row[i + 1])
        new_row.append(row[-1])
        rows.append(new_row)
        row = new_row

    print("\n".join([str(row) for row in rows]))


#        1
#      1    1
#    1    2    1
# 1     3    3    1


def test_pascal_triangle_1(capsys):
    pascal_triangle(1)
    captured = capsys.readouterr()
    assert captured.out == "[1]\n"
    pascal_triangle(10)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
"""
    )
