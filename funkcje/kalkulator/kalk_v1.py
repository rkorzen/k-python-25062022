operacja = input("Podaj operację [1-dodaj, 2-odejmij, 3-mnoz, 4-dziel]: ")
a = int(input("Podaj arg 1: "))
b = int(input("Podaj arg 2: "))

if operacja == "1":
    print("Wynik to: ", a + b)

elif operacja == "2":
    print("Wynik to: ", a - b)

elif operacja == "3":
    print("Wynik to: ", a * b)

elif operacja == "4":
    print("Wynik to: ", a / b)
