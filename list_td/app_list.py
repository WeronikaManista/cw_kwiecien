# lista z zadaniami
# możliwość dodania zadania
# zadanie ustawione na = niezrobione


lista_zadan_niezrobionych = {}
lista_zadan_zrobionych = {}

numerek = 1
print(f"Twoja to-do lista:\n")
print("help:\n"
      "n - new item"
      "d - display"
      "finish - mark as finished")

while True:

    sterowanie = input("co chesz zrobic")
    if sterowanie == "n":
        lista_zadan_niezrobionych[numerek] = input('Dodaj zadanie: ')
        numerek += 1

    elif sterowanie == "d":
        for klucz, wartosc in lista_zadan_niezrobionych.items():
            print(f'{klucz}. {wartosc}')

    elif sterowanie == "finish":
        lista_zadan_niezrobionych[numerek] =  



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
