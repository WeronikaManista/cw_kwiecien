'''
DWA SPOSOBY NA PRINT UNIKALNEJ LICZBY
'''

# li1 = []
# li2 = []
#
# while True:
#     x = input("wprowadz liczbe od 1 do 9: ")
#     (li1, li2).append(x)
#         if x not in li2
#
#     print(li1)
#     print(li2)


s = set()
list = []
inputy = 15
while inputy > 0:
    inputy -=1
    x = input("wprowadz:" )
    s.add(x)
    if x in s:
        list.append(x)

    print(s)
    print('lista prob', list)


