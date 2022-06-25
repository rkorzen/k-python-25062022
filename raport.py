# nazwa | kCal | białko | tłuszcz | węglowodany | cena / kg
products = [
    ["pomidor", 19, 1, 0, 4, 5.7, 350],
    ["ser mozarella", 248, 18, 19, 2, 38.32, 325],
    ["sałata", 13, 1, 0, 2, 3.15, 350]
]

raport = ""

bialko, tluscz, wegle, kalorie, koszt, waga_calosc = 0, 0, 0, 0, 0, 0

for p in products:
    waga = p[-1]
    cena = waga * p[-2] / 1000
    k = p[1] / 100 * waga
    b = p[2] / 100 * waga
    t = p[3] / 100 * waga
    w = p[4] / 100 * waga

    raport += (
        f"{p[0]:15}, kalorie:  {k:>6.2f}, b:  {b:>5.2f}, t:  {t:>5.2f}, w: {w:>5.2f},"
        f"waga:  {waga:4} g, koszt:  {cena:5.2f} PLN\n"
    )

    koszt += cena
    kalorie += k
    bialko += b
    tluscz += t
    wegle += w
    waga_calosc += waga

raport += "=" * 80 + "\n"
raport += (
    f"{'SUMA':15}, kalorie:  {kalorie:>6.2f}, b:  {bialko:>5.2f}, t:  {tluscz:>5.2f}, w: {wegle:>5.2f},"
    f"waga:  {waga_calosc:4} g, koszt:  {koszt:5.2f} PLN\n"
)

print(raport)