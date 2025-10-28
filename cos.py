import random

while(True):
    print("WITAJ W numguasser")
    print("A) wejdz")
    print("B) Wyjdz")
    numer = input("wybierz opcje")
    if numer == 'a':
        break
    def numguasser():
        PLAYING = 1
        zakres =  int(input("wprowadz do jakiej liczby chcesz zgadywac: "))
        losowa = random.randint(1,zakres)

        liczba_prob = 0
        while(PLAYING == 1):
            if  liczba_prob < 3:
                wybor = int(input("zgadnij liczbe: "))

                if wybor == losowa:
                    print(f'Zgadłeś ukrytą liczbe! to liczba {losowa}')
                    PLAYING = 0
                else:
                    liczba_prob += 1
                    print(f"Pozostało ci prób {3-liczba_prob}:")
            else:
                print("Nie udało ci sie zgadnąć")
                PLAYING = 0

    numguasser()