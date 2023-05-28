a = list(input("Sprawdź czy wyraz jest palindromem"))
if a == a[::-1]:
    print("palindrom")
else:
    print("nie jest palindromem")