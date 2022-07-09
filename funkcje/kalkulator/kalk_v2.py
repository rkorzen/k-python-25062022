def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


if __name__ == "__main__":
    operacja = input("Podaj operację [1-dodaj, 2-odejmij, 3-mnoz, 4-dziel]: ")
    a = int(input("Podaj arg 1: "))
    b = int(input("Podaj arg 2: "))

    if operacja == "1":
        result = add(a, b)

    elif operacja == "2":
        result = sub(a, b)

    elif operacja == "3":
        result = mul(a, b)

    elif operacja == "4":
        result = div(a, b)

    print("Wynik to: ", result)
