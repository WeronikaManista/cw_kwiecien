# # lista z zadaniami
# # możliwość dodania zadania
# # zadanie ustawione na = niezrobione
#
#
# list = [
#     "zadanie1", 'zadanie2',
# ]
# print("Your to - do list:")
# print(list)
#
# class Zadanie:
#     def __init__(self, nazwa):
#         self.nazwa = nazwa
#         self.czy_zrobione = False
#
# def wypisz (self):
#     if self.czy_zrobione:
#         znak = 'x'
#
#     return f'{nazwa} {znak}'
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for value in a_dict:
    print(value)

for key in a_dict:
    print(key, '->', a_dict[key])