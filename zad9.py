class czytelnik:
    def __init__(self, imie, nazwisko, ksiazka):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__ksiazka = ksiazka
    
os1 = czytelnik('Jan','Kowalski', "Harry potter")
os2 = czytelnik('Ala','Kowalska', "1984")

print(os1.ksiazka)
