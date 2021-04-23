import random
# SLOWNIKI SĄ BY OPEROWAĆ NA KLUCZACH, NIE WARTOŚCIACH. ---- DO WARTOŚCI SĄ LISTY
learn = {
    'dzien dobry': 'buenos dias',
    'chlopak': 'chico',
    'czesc': 'hola',
    "dupa": "culo"
}
learned = {}
repeats = {}


for _ in range(0, len(learn.keys())):
    lang = random.choice(["PL", "ES"])
    print(lang)
    if lang == "PL":
        random_key = random.choice(list(learn.keys()))

        z = input(f"{learn.get(random_key)} po polsku: ")
        if z == random_key:
            print('Poprawnie.')
            item = learn.pop(random_key)
            learned.update({random_key: item})
            # learned['dzien'] = item

        else:  # elif z != 'dzien dobry':
            item = learn.get(random_key)
            repeats.update({random_key: item})

# odwrotnie logicznie do PL:
    elif lang == "ES":
        polish_word = random.choice(list(learn.keys()))
        spain_word = learn.get(polish_word)

        z = input(f"{polish_word} po hiszpansku: ")
        if z == spain_word:
            print('Poprawnie.')
            item = learn.pop(polish_word)
            learned.update({polish_word: item})

        else:  # elif z != 'dzien dobry':
            item = learn.get(polish_word)
            repeats.update({polish_word: item})

    print(f'Do nauczenia: {learn}')

if repeats:
    for powtorka in range(1, 3):

        print("POWTORKA")
        print(repeats)
        random_key = random.choice(list(repeats.keys()))
        p = input(f"{repeats.get(random_key)} po polsku: ")
        if p == random_key:
            print('Poprawnie.')
            item = repeats.pop(random_key)
            learned.update({random_key: item})

if len(learn.keys()) == 0 and len(repeats.keys()) == 0:
    print('SUKCES')
else:
    print("Musisz jeszcze poćwiczyć")

print('Koniec')



# NOTATKI Z PRÓB:
"""
import random
d = {'VENEZUELA':'CARACAS', 'CANADA':'OTTAWA'}
random.choice(list(d.values()))
"""

# dict_keys(['dzien', 'chlopak'])  <----wyjdzie to z tego: print(learn.keys())
# ['dzien', 'chlopak'] <-- wyjdzie to z tego:              print(list(learn.keys()))

# random.choices(list(learn.keys()))
# print(random.choices(list(learn.keys())))

##