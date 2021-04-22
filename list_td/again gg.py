import random

learn = {'dzien dobry': 'buendos dias', 'chlopak': 'chico', 'siema' : 'hola', "dupa" : "culo"}
learned = {}
repeats = {}

"""
import random
d = {'VENEZUELA':'CARACAS', 'CANADA':'OTTAWA'}
random.choice(list(d.values()))
"""

# dict_keys(['dzien', 'chlopak'])  <----wyjdzie to z tego: print(learn.keys())
# ['dzien', 'chlopak'] <-- wyjdzie to z tego:              print(list(learn.keys()))


# random.choices(list(learn.keys()))
# print(random.choices(list(learn.keys())))


for _ in range(0, len(learn.keys())):
    random_key = random.choices(list(learn.keys()))[0]

    z = input(f"{learn.get(random_key)} po polsku: ")
    if z == random_key:
        print('Poprawnie.')
        item = learn.pop(random_key)
        learned.update({random_key: item})
        # learned['dzien'] = item



    else: # elif z != 'dzien dobry':
        item = learn.get(random_key)
        repeats.update({random_key: item})

    print(f'Do nauczenia: {learn},\n Nauczone: {learned},\n W folderze repeats: {repeats}')

#------------------------------------------------------

# j = input(f"{learn.get(random_key)} po polsku: ")
# if j == random_key:
#     print('Poprawnie.')
#     item = learn.pop(random_key)
#     learned.update({random_key: item})
#     # learned['dzien'] = item

print("POWTORKA")

for powtorka in range(1,3):

    if len(repeats.keys()) > 0:
        print('Cwiczenia ze slownikiem repeats')
        print('Repity', repeats)

        p = input(f"{learn.get(random_key)} po polsku: ")
        if p == random_key:
            print('Poprawnie.')
            item = repeats.get(random_key)
            learned.update({random_key: item})


    # if len(repeats.keys()) > 0:
    #     gg = input((f"{learn.get(random_key)} Chlopak to po hiszpansku: ")
    #         if gg == random_key:
    #         print('Poprawnie.')
    #         kreml = repeats.get(random_key)
    #         learned.update({random_key: kreml})



print('Koniec')
print(f'Do nauczenia: {learn}\nNauczone: {learned}\nW folderze repeats: {repeats}')

