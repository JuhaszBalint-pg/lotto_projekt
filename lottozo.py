'''
2-3 fős csoportokban készítsetek egy lottó játékot!
Legyen lehetőség a játékos tippjeinek a felvételére!
Utána a program sorsoljon ki számokat!
Végül írjuk ki, hogy mennyi találat volt!
Ha tudjátok, többféle lottó játékkal is lehessen játszani!
'''

import random

print('Üdvözlünk a lottó játékunkban')

jatekos_tipp = []
tippnum = 0
print('Add meg a tippjeid!')
while tippnum != 5:
    useri = int(input(''))
    if 0 < useri < 100:
        tippnum += 1
        jatekos_tipp.append(useri)
    else: 
        print('0-100 között ajd meg számokat!')
print(jatekos_tipp)

gepsors = []
for i in range (1,6):
        gepsors.append(random.randint(1, 100))

for i in gepsors:
    if gepsors.count(i) > 1:
        try:
            gepsors.pop(i)

        except IndexError:
            continue

print(gepsors)
