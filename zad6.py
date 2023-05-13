from r4_1 import *
print("1-dodawanie 2-odejmowanie 3-mnożenie 4-dzielenie 0-zakończ")
while(True):
    a = int(input("wybierz operacje"))
    if a == 0: break
    """zakończenie programu"""
    l1 = int(input("podaj 1 liczba"))
    l2 = int(input("podaj 2 liczbe"))
    if a == 1:
        print(dodawanie(l1, l2))
    elif a == 2:
        print(odejmowanie(l1, l2))
    elif a == 3:
        print(mnożenie(l1, l2))
    elif a == 4:
        print(dzielenie(l1, l2))
   