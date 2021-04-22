from time import sleep

for i in reversed(range(0,11)):
    print(i)
    sleep(2)
    if i < 2:
        sleep(3)

print('Kaboom')


