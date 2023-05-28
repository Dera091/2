def dodawanie (x: float, y: float) -> float:
    """dodawanie"""
    return x + y
    
def odejmowanie(x: float, y: float) -> float:
    """odejmowanie"""
    return x - y
    
def mnożenie(x: float, y: float) -> float:
    """mnożenie"""
    return x * y
    
def dzielenie(x: float, y: float) -> float:
    """dzielenie"""
    return x / y
    
print("1-dodawanie 2-odejmowanie 3-mnożenie 4-dzielenie 0-zakończ")
while(True):
    a = int(input("wybierz operacje"))
    if a == 0: break
    
    l1 = float(input("podaj 1 liczba"))
    l2 = float(input("podaj 2 liczbe"))
    if a == 1:
        print(dodawanie(l1, l2))
    elif a == 2:
        print(odejmowanie(l1, l2))
    elif a == 3:
        print(mnożenie(l1, l2))
    elif a == 4:
        if l2 == 0:
            continue
            print("nie można dzielić przez zero")
        else:
            print(dzielenie(l1, l2))
