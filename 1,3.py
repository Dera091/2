import random
x = random.randint(0,100)
i = 0
while(True):
    i = i + 1
    a = int(input("podaj liczbe"))
    if a == x:
        print("brawo, liczba została trafiona za",i,"razem")
        c = input("napisz tak jesli chcesz zagrac ponownie")
        if c == "tak":
            x = random.randint(0,100)
            i = 0
            continue
        else:
            break
    elif a < x:
        print("twoja liczba jest mniejsza od szukanej")
    elif a > x:
        print("twoja liczba jest większa od szukanej")