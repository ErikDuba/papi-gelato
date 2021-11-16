print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')

bolletjes = int(input('Hoeveel bolletjes wilt u?: '))

if 1 <= bolletjes <= 3:
    keuze1 = input('Wilt u deze ' + str(bolletjes) + 'in A een hoorntje of B een bakje? A/B: ')
    if keuze1 == 'A':
        keuze2 = input('Hier is uw hoorntje met' + str(bolletjes) + ' bolletje(s). Wilt u nog meer bestellen? (J/N): ')
        if keuze2 == 'Y':
            continue
    elif keuze1 == 'B':
        keuze3 = input('Hier is uw bakje met' + str(bolletjes) + ' bolletje(s). Wilt u nog meer bestellen? (J/N): ')
elif 4 <= bolletjes <= 8:
    print('Dan krijgt u van mij een bakje met ' + str(bolletjes) + ' bolletjes')
elif bolletjes > 8:
    print('Sorry, zulke grote bakken hebben we niet')
else:
    print('Sorry, dat begrijp ik niet...')

input('')
