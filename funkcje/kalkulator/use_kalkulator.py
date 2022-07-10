from kalk_v3 import operations
import logging

logging.basicConfig(level=logging.INFO, filename="kalkulator.logs")
logger = logging.getLogger(__name__)
# odczytaj dane z data.txt i wykonaj obliczenia zgodnie z zawartoscia wierszy
# wiersze zbudowane sa wg schematu;
# operacja a b

try:
    with open("data.txt") as f:
        data = f.read().splitlines()

        for d in data:
            op, a, b = d.split()
            a, b = int(a), int(b)
            print(operations[op](a, b))
except:
    logger.error("Wystapił błąd", exc_info=True)


