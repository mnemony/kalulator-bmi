def bmicalc():

    while True:

        print("wpisz 'q' by przerwać")
        print("Podaj swój wzrost w cm")
        wzrost = input('Wzrost w cm: ')
        print("podaj swoją wagę w kg")
        waga = input('Masa w kg: ')
        
        if wzrost == 'q' or waga == 'q':
            break
        else:
            try:
                wzrost = float(wzrost)/ 100 

                bmi = float(waga) / float(wzrost)**2
                bmi = round(bmi, 1)
                print("\ntwoje bmi to " + str(bmi))
                if bmi <= 18.5:
                    print("niedowaga")
                elif bmi <= 24.9:
                    print('waga w normie')
                elif bmi <= 29.9:
                    print('nadwaga')
                else:
                    print('otyłość')

            except ValueError:
                print('\nniewłaściwe dane - użyj cyfr np. "180" i "75"')            

bmicalc()