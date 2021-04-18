import cowsay


def funkcja_dodawania(num1, num2):
    return int(num1) + int(num2)


def funkcja_odejmowania(num1, num2):
    odejmij = int(num1) - int(num2)

    return odejmij


def funkcja_mnozenia(num1, num2):
    mnoz = int(num1) * int(num2)

    return mnoz


def funkcja_dzielenia(num1, num2):
    dziel = int(num1) / int(num2)

    return dziel


zapamietaj = 0

while True:
    num1 = input("Kalkulator\nDana_1: ")
    oper = input("Operacja: +, -, :, *: ")
    num2 = input("Dana_2: ")

    if oper == "+":
        # dodaj = int(num1) + int(num2)
        wynik = funkcja_dodawania(num1, num2)

        zapamietaj = zapamietaj + wynik
        cowsay.cow(f"= {wynik}")
        print(zapamietaj)

    elif oper == "-":
        odejmij = int(num1) - int(num2)
        wynik = funkcja_odejmowania(num1, num2)
        cowsay.dragon(f"= {wynik}")

    elif oper == "*":
        mnoz = int(num1) * int(num2)
        wynik = funkcja_mnozenia(num1, num2)
        cowsay.ghostbusters("= %s" % wynik)

    elif oper == '/':
        dziel = int(num1) / int(num2)
        wynik = funkcja_dzielenia(num1, num2)
        cowsay.kitty("= {}".format(wynik))

    else:
        print("Nie ma takiej mozliwosci")
