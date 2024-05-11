import bohater
import wstep
import skrzynia
import smierc
import kupiec
import os

wybor_klasy = wstep.wstep()

if wybor_klasy == wstep.klasa[0]:
    gracz = bohater.Bohater(hp=8, atak=7)
elif wybor_klasy == wstep.klasa[1]:
    gracz = bohater.Bohater(atak=3, pieniadze=4)
elif wybor_klasy == wstep.klasa[2]:
    gracz = bohater.Bohater(hp=13, atak=3)
elif wybor_klasy == wstep.klasa[3]:
    gracz = bohater.Bohater(hp=12, atak=6, pieniadze=0)
elif wybor_klasy == wstep.klasa[4]:
    gracz = bohater.Bohater()

while 1:
    # os.system('cls||clear')

    print(f"\nPunkty życia: {gracz.hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
          f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
          f"{gracz.exp}/{gracz.poziom * 10}, Poziom: {gracz.poziom}\n\n")

    opcja = input("Wybierz opcję: \n"
                  "1. Idź prosto\n"
                  "2. Idź w prawo\n")
    if opcja.isdigit() and int(opcja) == 1:
        skrzynia.skrzynia(gracz)
        smierc.czy_smierc(gracz)
        continue
    elif opcja.isdigit() and int(opcja) == 2:
        opcja1 = input("Wybierz opcję: \n"
                       "1. Idź w lewo\n"
                       "2. Idź przez drzwi\n")
        if opcja1.isdigit() and int(opcja1) == 1:
            kupiec.kupiec(gracz)
            smierc.czy_smierc(gracz)
            continue
        elif opcja1.isdigit() and int(opcja1) == 2:
            print("Wyważasz drzwi i idziesz dalej")
            continue
        else:
            print("Niepoprawny wybór!")
    else:
        print("Niepoprawna opcja!")
