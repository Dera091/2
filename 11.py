def dodawanie (x, y) -> None:
    return x + y
    
def odejmowanie(x, y) -> None:
    return x - y
   
def mnożenie(x, y) -> None:
    return x * y
    
def dzielenie(x, y) -> None:
    return x / y
    
print("1-dodawanie 2-odejmowanie 3-mnożenie 4-dzielenie 0-zakończ")
while(True):
    a = input("wybierz operacje")
    if  a == "0":  break
    
    try:
        l1 = float(input("podaj 1 liczba"))
        l2 = float(input("podaj 2 liczbe"))
    except ValueError:
        print("nieprawidłowe dane")
        continue
    try:
        if a == "1":
            print(dodawanie(l1, l2))
        elif a == "2":
            print(odejmowanie(l1, l2))
        elif a == "3":
            print(mnożenie(l1, l2))
        elif a == "4":
            print(dzielenie(l1, l2))
        else:
            print("nieprawidłowo wybrana operacja, spróbuj ponownie")
    except (ZeroDivisionError):
        print("nie można dzielić przez zero")