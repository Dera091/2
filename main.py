import json
zadania = {}

def dodaj():
    id = len(zadania) + 1
    tytuł = input("podaj tytuł")
    opis = input("podaj opis")
    termin = input("podaj termin")
    zadania[id] = {"tytuł":tytuł, "opis":opis, "termin":termin}

def sprawdź():
    for id, b in zadania.items():
        print("id ",id)
        print("tytuł ",b["tytuł"])
        print("termin ",b["termin"])
def sprawdźopis():
    try:
        id = int(input("podaj id"))
        b = zadania[id]
        print("opis zadania", b["opis"])
    except KeyError:
        print("nieprawidłowe id")

def usuń():
    try:
        id = int(input("podaj id"))
        del zadania[id]
    except KeyError:
        print("nieprawidłowe id")

def edytuj():
    id = int(input("podaj id"))
    if id in zadania:
        
        tytuł = input("podaj nowy tytuł")
        opis = input("podaj nowy opis")
        termin = input("podaj nowy termin")
        zadania[id] = {"tytuł":tytuł, "opis":opis, "termin":termin}
    else:
        print("nieprawidłowe id")
try:
    with open("plik.json","r") as infile:
        zadania1 = json.load(infile)
        if zadania1:
            zadania = {int(id): b for id, b in zadania1.items()}
            for id, b in zadania.items():
                print("id ",id)
                print("tytuł ",b["tytuł"])
                print("termin ",b["termin"])
        else:
            print("brak zadań")
except FileNotFoundError:
    pass
    print("brak zadań")
while True:
    print("---------------")
    print("1-dodaj zadanie")
    print("2-sprawdź zadania")
    print("3-sprawdź opis zadania")
    print("4-usuń zadanie")
    print("5-edytuj zadanie")
    print("6-zakończ")
    print("---------------")
    
    a = int(input("wybierz polecenie "))
    if a == 1:
        dodaj()
    elif a == 2:
        sprawdź()
    elif a == 3:
        sprawdźopis()
    elif a == 4:
        usuń()
    elif a == 5:
        edytuj()
    elif a == 6:
        with open("plik.json","w") as outfile:
            json.dump(zadania, outfile)
        print("zakończono program, utworzono plik JSON")
        break
    else:
        print("nieprawidłowe polecenie")
    