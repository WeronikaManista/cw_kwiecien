
def funkcja_dodawania(num1, num2):
    dodaj = int(num1) + int(num2)

    return dodaj

def funkcja_odejmowania(num1, num2):
    odejmij = int(num1) - int(num2)

    return odejmij


Message = input("Cześć, co chcesz zrobić? Możliwości: dodać [d], odjąć [o]")
if Message == "d":
    num1 = input("liczba 1: ")
    num2 = input("liczba 2: ")

    print("Rezultat to: ", funkcja_dodawania(num1, num2))


elif Message == "o":
    num1 = input("liczba 1: ")
    num2 = input("liczba 2: ")

    print("Rezultat to: ", funkcja_odejmowania(num1, num2))


# num1 = input("liczba 1: ")
# num2 = input("liczba 2: ")




#print("Rezultat to: ", funkcja_dodawania (num1, num2) or funkcja_odejmowania(num1, num2))









