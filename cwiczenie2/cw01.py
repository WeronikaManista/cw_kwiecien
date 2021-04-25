transakcje = []

wybor = None

while wybor != '0':
    print(' 0 koniec operacji\n1 wplac kase\n 2 wyplac hajs\n 3 spr saldo\n 4. pokaz wplywy\n 5 pokaz obciazenia')
    wybor = input('wybierz opcje: ')

    if wybor == '1':
        kwota = input('podaj kwote do wplaty')
        transakcje.append(int(kwota))

    elif wybor == '2':
        kwota = input('wyplac hajs:')
        transakcje.append(-int(kwota))

    elif wybor == '3':
        print(f'saldo = {sum(transakcje)}')

    elif wybor == '4':
       uznania = []
       for kwota in transakcje:
        if kwota > 0:
            uznania.append(kwota)
        print(sum(uznania))


    elif wybor == '5':
        obciazenia = 0
        for kwota in transakcje:
            if kwota < 0:
                obciazenia += kwota
            print(obciazenia)

    print(transakcje)