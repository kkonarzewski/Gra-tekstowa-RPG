import random
import przeciwnik
import bohater
import smierc
import level_up
import boss


def walka_wstep(gracz, czy_boss=False):
    if not czy_boss:
        print("\nNapotykasz przeciwnika. Czy chcesz walczyć?\n")
        while 1:
            opcja = input("1. Tak\n"
                          "2. Nie (75% szans na ucieczkę)\n")
            if opcja.isdigit() and int(opcja) == 1:
                walka(gracz, czy_boss)
                return
            if opcja.isdigit() and int(opcja) == 2:
                wynik = random.randint(1, 4)
                if wynik == 4:
                    print("Udało Ci się przejść obok wroga niezauważonym. Ominąłeś walkę\n")
                    return
                else:
                    print("Podczas próby przejścia obok zostałeś zauważony. Walka!\n")
                    walka(gracz, czy_boss)
            else:
                print("Niepoprawny wybór\n")
    else:
        print("\nStajesz do walki z bossem tego poziomu!\n")
        walka(gracz, czy_boss)
        return


def walka(gracz, czy_boss):
    if czy_boss == "latwy":
        wrog = boss.BossLatwy(4 + gracz.poziom, 1 + gracz.poziom)
    elif czy_boss == "sredni":
        wrog = boss.BossSredni(4 + gracz.poziom, 1 + gracz.poziom)
    else:
        wrog = przeciwnik.Przeciwnik(4 + gracz.poziom, 1 + gracz.poziom)
    while gracz.hp > 0 and wrog.hp > 0:
        print(f"\nTwoje punkty życia: {gracz.hp}/{gracz.max_hp}\n"
              f"Punkty życia przeciwnika: {wrog.hp}/{wrog.max_hp}\n")
        tura_gracza(gracz, wrog)
        if wrog.hp <= 0:
            break
        print(f"\nTwoje punkty życia: {gracz.hp}/{gracz.max_hp}\n"
              f"Punkty życia przeciwnika: {wrog.hp}/{wrog.max_hp}\n")
        tura_wroga(gracz, wrog)
    if wrog.hp <= 0:
        if not czy_boss:
            print(f'Wygrałeś walkę! Zdobywasz {wrog.max_hp} punktów doświadczenia')
            gracz.exp += wrog.max_hp
            if gracz.exp >= 10 + (gracz.poziom - 1) * 2:
                level_up.level_up(gracz)
            return
    else:
        smierc.czy_smierc(gracz)


def tura_gracza(gracz, wrog):
    wybor = input("\nJaką akcję chcesz przeprowadzić?\n"
                  "1. Lekki atak (70% szans powodzenia - 50% obrażeń)\n"
                  "2. Średni atak (50% szans powodzenia - 75% obrażeń)\n"
                  "3. Silny atak (30% szans powodzenia - 100% obrażeń)\n"
                  f"4. Odpoczynek (+ 1 punkt życia)\n")
    if wybor.isdigit() and int(wybor) == 1:
        r = random.randint(1, 10)
        if 1 <= r <= 7:
            obrazenia = int((gracz.atak + bohater.bronie[gracz.bron]) * 0.5)
            wrog.hp -= obrazenia
            print(f"Zadałeś {obrazenia} obrażeń przeciwnikowi")
        else:
            print("Nie trafiłeś!")
    elif wybor.isdigit() and int(wybor) == 2:
        r = random.randint(1, 10)
        if 1 <= r <= 5:
            obrazenia = int((gracz.atak + bohater.bronie[gracz.bron]) * 0.75)
            wrog.hp -= obrazenia
            print(f"Zadałeś {obrazenia} obrażeń przeciwnikowi")
        else:
            print("Nie trafiłeś!")
    elif wybor.isdigit() and int(wybor) == 3:
        r = random.randint(1, 10)
        if 1 <= r <= 3:
            obrazenia = int(gracz.atak + bohater.bronie[gracz.bron])
            wrog.hp -= obrazenia
            print(f"Zadałeś {obrazenia} obrażeń przeciwnikowi")
        else:
            print("Nie trafiłeś!")
    elif wybor.isdigit() and int(wybor) == 4:
        if gracz.hp == gracz.max_hp:
            print("Nie możesz odpoczywać, ponieważ posiadasz maksymalną ilość punktów życia\n")
            tura_gracza(gracz, wrog)
        else:
            gracz.hp += 1
            print("Zregenerowałeś 1 punkt życia\n")
    else:
        print("Niepoprawny wybór!\n")


def tura_wroga(gracz, wrog):
    wybor = random.randint(1, 4)
    if wybor == 1:
        r = random.randint(1, 10)
        if 1 <= r <= 7:
            obrazenia = int(wrog.atak * 0.5)
            gracz.hp -= obrazenia
            print(f"Przeciwnik zadał {obrazenia} obrażeń lekkim atakiem")
        else:
            print("Przeciwnik nie trafił lekkim atakiem!")
    elif wybor == 2:
        r = random.randint(1, 10)
        if 1 <= r <= 5:
            obrazenia = int(wrog.atak * 0.75)
            gracz.hp -= obrazenia
            print(f"Przeciwnik zadał {obrazenia} obrażeń średnim atakiem")
        else:
            print("Przeciwnik nie trafił średnim atakiem!")
    elif wybor == 3:
        r = random.randint(1, 10)
        if 1 <= r <= 3:
            obrazenia = int(wrog.atak)
            gracz.hp -= obrazenia
            print(f"Przeciwnik zadał {obrazenia} obrażeń silnym atakiem")
        else:
            print("Przeciwnik nie trafił silnym atakiem!")
    elif wybor == 4 and wrog.hp <= wrog.max_hp - 1:
        wrog.hp += 1
        print("Przeciwnik zregenerował 1 punkt życia\n")
    elif wybor == 4 and wrog.hp == wrog.max_hp:
        tura_wroga(gracz, wrog)
