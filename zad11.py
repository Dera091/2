def dodawanie (x, y) -> None:
    return x + y
    """dodawanie"""
def odejmowanie(x, y) -> None:
    return x - y
    """odejmowanie"""
def mnożenie(x, y) -> None:
    return x * y
    """mnożenie"""
def dzielenie(x, y) -> None:
    return x / y
    """dzielenie"""
print("1-dodawanie 2-odejmowanie 3-mnożenie 4-dzielenie 0-zakończ")
while(True):
    a = int(input("wybierz operacje"))
    if  a == 0:  break
    if  a <= -1 or a >= 5:
        print("nieprawidłowa liczba")
        break
    """zakończenie programu"""
    l1 = float(input("podaj 1 liczba"))
    l2 = float(input("podaj 2 liczbe"))
    try:
        if a == 1:
            print(dodawanie(l1, l2))
        elif a == 2:
            print(odejmowanie(l1, l2))
        elif a == 3:
            print(mnożenie(l1, l2))
        elif a == 4:
            print(dzielenie(l1, l2))
    except (ZeroDivisionError):
        print("nie można dzielić przez zero")
  