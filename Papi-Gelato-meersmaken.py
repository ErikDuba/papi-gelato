print('Welkom bij Papi Gelato!')

i = 1
while i == 1:
    a = 1
    bolletjes = int(input('Hoeveel bolletjes wilt u?: '))
    if 1 <= bolletjes <= 3:
        keuze1 = input('Wilt u deze ' + str(bolletjes) + ' in (A) een hoorntje of (B) een bakje? A/B: ')
        if keuze1 == 'A':
            keuze2 = input('Hier is uw hoorntje met ' + str(bolletjes) + ' bolletje(s). Wilt u nog meer bestellen? (J/N): ')
            if keuze2 == 'J':
                continue
            elif keuze2 == 'N':
                print('Bedankt en tot ziens!')
                break
        elif keuze1 == 'B':
            keuze3 = input('Hier is uw bakje met ' + str(bolletjes) + ' bolletje(s). Wilt u nog meer bestellen? (J/N): ')
            if keuze3 == 'J':
                continue
            elif keuze3 == 'N':
                print ('Bedankt en tot ziens!') 
                break
    elif 4 <= bolletjes <= 8:
        while a == 1:
            smaak2 = input('Wij hebben (A) Aardbei, (C) Chocolade, (M) Munt of (V) Vanille.\nIn welke smaak wilt u deze bolletjes? A/C/M/V: ')
            if smaak2 == 'A':
                keuze4 = input('Dan krijgt u van mij een bakje met ' + str(bolletjes) + ' bolletjes aardbei. Wilt u nog meer bestellen? (J/N): ')
                if keuze4 == 'J':
                    continue
                elif keuze4 == 'N':
                    break
            elif smaak2 == 'C':
                keuze5 = input('Dan krijgt u van mij een bakje met ' + str(bolletjes) + ' bolletjes chocolade. Wilt u nog meer bestellen? (J/N): ')
                if keuze5 == 'J':
                    continue
                elif keuze5 == 'N':
                    break
            elif smaak2 == 'M':
                keuze6 = input('Dan krijgt u van mij een bakje met ' + str(bolletjes) + ' bolletjes munt. Wilt u nog meer bestellen? (J/N): ')
                if keuze6 == 'J':
                    continue
                elif keuze6 == 'N':
                    break
            elif smaak2 == 'V':
                keuze7 = input('Dan krijgt u van mij een bakje met ' + str(bolletjes) + ' bolletjes vanille. Wilt u nog meer bestellen? (J/N): ')
                if keuze7 == 'J':
                    continue
                elif keuze7 == 'N':
                    break
            else:
                print('Sorry, dat snap ik niet...')
    elif bolletjes > 8:
        print('Sorry, zulke grote bakken hebben we niet')
        continue
    else:
        print('Sorry, dat begrijp ik niet...')
        continue
    
input('')