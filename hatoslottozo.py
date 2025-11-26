import random
futas = True
while futas:
    print('Üdvözlünk a lottó játékunkban')

    jatekos_tipp = []
    tippnum = 0
    print('Add meg a tippjeid!')
    while tippnum != 6:
        useri = int(input(''))
        if 0 < useri < 100:
            tippnum += 1
            jatekos_tipp.append(useri)
        else: 
            print('0-100 között ajd meg számokat!')
    print(jatekos_tipp)

    gepsors = []
    for i in range (1,7):
            gepsors.append(random.randint(1, 45))

    for i in gepsors:
        if gepsors.count(i) > 1:
            try:
                gepsors.pop(i)

            except IndexError:
                continue

    print(gepsors)

    pontszam = 0
    for i in gepsors:
        gepsors.count(i)
        if i in jatekos_tipp:
            pontszam += 1
    print(f"ennyi a pontszámod: {pontszam}")
    x = input("szeretnél még játszani? (i/n) \n")
    if x == "n":
        futas = False