import random
import smierc


def skrzynia(gracz):
    print("\nNa swojej drodze spotykasz starą skrzynię. Czy chcesz ją otworzyć?")
    while 1:
        opcja = input("1. Tak\n"
                      "2. Nie\n")
        if opcja.isdigit() and int(opcja) == 1:
            wynik = random.randint(0, 4) - 1
            if wynik == 1:
                print(f'Znalazłeś 1 monetę')
                gracz.pieniadze += 1
                return
            elif wynik == 2 or wynik == 3:
                print(f'Znalazłeś {wynik} monety')
                gracz.pieniadze += wynik
                return
            elif wynik == 0:
                print("Skrzynia okazała się pusta! Nic nie zdobyłeś")
                return
            else:
                print("To była skrzynia pułapka! Tracisz 1 punkt życia")
                gracz.hp -= 1
                smierc.czy_smierc(gracz)
                return
        elif opcja.isdigit() and int(opcja) == 2:
            print("Nie chcesz ryzykować i idziesz dalej")
            return
        else:
            print("Niepoprawny wybór!")
