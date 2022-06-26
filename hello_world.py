import hello_world

print("Hello World")


if 1 > 0 or 1 / 0:
    print("cos")
    x = 10

m1 = [
    [1, 2],
    [3, 4],
]
m2 = [
    [3, 4],
    [3, 4],
]


assert add_matrices(m1, m2) == [
    [4, 6],
    [6, 8],
]
