#### HISZPANSKI W 3 SLOWKA ####

# 1. Pokaż słówka w słowniku - do zapamiętania
# 2. Zapytaj uzytkownika o slowko hiszp pokazując tylko klucz
#       jeśli zgadnie value:
#           Dodaj słówko do dict 2
#        nie zgadnie:
#       slowko idzie do dict: powtorz


dict_to_learn = {'dzien': 'buendos dias', 'chlopiec': 'chico'}
dict_learnt = {}
dict_repeat = {}

# answer = input('L - learn\t D2 - words learnt:')
antwort = 'dzien dobry'
ant2 = 'chlopiec'
ant3 = 'chico'


# while not antwort == True or not  ant2 == True or ant3 == True:
#     if answer == 'L':


print('Para do nauczenia: ')
z = input('Buenos dias to po polsku: ')

while True:
    if z == antwort:
        ze = dict_to_learn.pop("dzien")
        dict_learnt.update({z: ze})
        print('slowo w nauczonych', dict_learnt)
    else:
        print('Nie tak w biblii napisano. Again: ')
        ze = dict_to_learn.pop("dzien")
        dict_repeat.update(dict_to_learn["dzien"])
        print('Slowo twoje w dict_repeat:', (dict_repeat))

    #---------------------------------------------

print('Para do nauczenia: ')
g = input('Chico to po polsku: ')
if g == ant2:
    he = dict_to_learn.pop('chlopiec')
    dict_learnt.update({g: he})
    print(f'Wyrazy nauczone: {dict_learnt}')

else:
    ze = dict_to_learn.pop('chlopiec')
    dict_repeat.update({g: ze})
    print('Slowo twoje w dict_repeat:', (dict_repeat))

    # elif answer == 'D2':
    #     print(dict_learnt)






#
#     if h == dict_to_learn.values:
#     #for value in dict_to_learn['chopiec']:
#         print(value)
#
#     # if h == ant3:
#     #     ze = dict_to_learn.pop('chlopiec')
#     #     dict_learnt.update({h: ze})
#     #     print(f'Wyrazy nauczone: {dict_learnt}')
#

# x = input('Chłopak to po hiszpansku: ')
# if x == 'chico':
#     print('Poprawnie.')
#     tym = learn.pop('chlopak')
#     learned.update({'chlopak': tym})
#
# elif z != 'chico':
#     tym = learn.pop()
#     repeats.update({'chlopak': tym})
#
#
# #item = set(dict_to_learn.pop(antwort))
# dict_learnt.update({antwort, item}))