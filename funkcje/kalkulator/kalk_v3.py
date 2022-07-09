import logging

# logging.basicConfig(level=logging.INFO, filename="kalkulator.logs")
logger = logging.getLogger(__name__)
"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""


# logger.debug("Malo wazne")
# logger.info("Informacja")
# logger.warning("Ostrzezenie")
# logger.error("Informacja o błędzie")
# logger.critical("krytyczne zdarzenie")


def add(a, b):
    logger.info(f"Wywołanie add z argumentami: {a} {b}")
    return a + b


def sub(a, b):
    logger.info(f"Wywołanie sub z argumentami: {a} {b}")
    return a - b


def mul(a, b):
    logger.info(f"Wywołanie mul z argumentami: {a} {b}")
    return a * b


def div(a, b):
    logger.info(f"Wywołanie div z argumentami: {a} {b}")
    try:
        result = a / b
    except ZeroDivisionError:
        logger.error("Dzielenie przez 0", exc_info=True)
    return result


def get_data():
    operacja = input("Podaj operację [1-dodaj, 2-odejmij, 3-mnoz, 4-dziel]: ")
    if operacja not in "1234":
        raise ValueError("Złą operacja")
    a = int(input("Podaj arg 1: "))
    b = int(input("Podaj arg 2: "))
    return operacja, a, b


def main():
    op, a, b = get_data()
    result = operations[op](a, b)
    print("Wynik to: ", result)


operations: dict = {"1": add, "2": sub, "3": mul, "4": div}
a: int = 10


if __name__ == "__main__":
    print(dir())
    print(__name__)
    print(__file__)
    main()
