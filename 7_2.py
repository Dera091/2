import random
from os import path
c = int(input("podaj ilość kombinacji"))
if c > 625:
    print("maksymalna ilość kombinacji to 625")
else:
    
    with open('imiona.txt', 'r', encoding="utf-8") as imiona, open('nazwiska.txt', 'r', encoding="utf-8") as nazwiska:
        imie = [a.strip() for a in imiona.readlines()]
        nazwisko = [b.strip() for b in nazwiska.readlines()]

        losowe = set()
        while len(losowe) < c:
            imie1 = random.choices(imie)
            nazwisko1 = random.choices(nazwisko)
            x = f"{imie1} {nazwisko1}\n"
            losowe.add(x)

    

    for x in losowe:
        print(x)

with open('kombinacja.txt', 'w', encoding='utf-8') as kombinacja:
   for x in losowe:
    kombinacja.write(x)

