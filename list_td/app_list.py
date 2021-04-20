# lista z zadaniami
# możliwość dodania zadania
# zadanie ustawione na = niezrobione


lista_zadan_niezrobionych = {}
lista_zadan_zrobionych = {}

numerek = 1
print(f"Twoja to-do lista:\n")
print("INSTRUCTIONS:\n"
      "n - add new item \n"
      "d - display niezrobione \n"
      "d2 - display zrobione \n"
      "finish - mark as finished \n"
      "q - quit")

while True:

    sterowanie = input("CO CHCESZ ZROBIC?: ")
    if sterowanie == "n":
        lista_zadan_niezrobionych[numerek] = input('Dodaj zadanie: ')
        numerek += 1

    elif sterowanie == "d":
        for klucz, wartosc in lista_zadan_niezrobionych.items():
            print(f'{klucz}. {wartosc}')


    elif sterowanie == "d2":
        for klucz, wartosc in lista_zadan_zrobionych.items():
            print(f'{klucz}. {wartosc}')

    elif sterowanie == "finish":
        # value = (lista_zadan_niezrobionych)
        print(f'Nasze klucze: {set(lista_zadan_niezrobionych.keys())}')
        wybor = int(input('Ktory item chcesz ozn. = zrobione?: '))
        item = lista_zadan_niezrobionych.pop(wybor)
        lista_zadan_zrobionych.update({wybor: item})

# slownik.keys()
# input ktory chesz usunac
# zmienna =pop(wybor usera)
# drugi slownik.upadete({wybor usera; tmp})


    elif sterowanie == "q":
        print('Still to do: ', lista_zadan_niezrobionych)
        print('Congrats. It\'s done: ', lista_zadan_zrobionych)
        quit()

# lista_zadan_niezrobionych.append(input("Dodaj zadanie: "))
# dddd.update({
#     numerek: fooo
# })

# dict["klucz"] = "warosc"

# niezrobione = False
#
# class Zadania:
#     i = zadanie()
#     zadanie.nazwa = 'hhh'
#     zadanie.czy_zrobione = False
#
#     def Zadania(self, x, y):
#         self.x = niezrobione
#         self.y = niezrobione
#         print(Zadania)
#
#
#
#
#
# # class Zadanie:
# #     set = not_done
# #
# #
# #
# # not_done = 0
# # set zadanie = not_done
#
# # def dodaj_zadanie(self, zadanie):
# #     dodaj =
# #
# input(dodaj)
