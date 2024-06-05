import random
import smierc


def kapliczka(gracz):
    print("\nWchodzisz do pomieszczenia, w którym znajduje się dziwny ołtarz.\n"
          "Czy chcesz się pomodlić?\n")
    while 1:
        wybor = input("1. Tak\n"
                      "2. Nie\n")
        if wybor.isdigit() and int(wybor) == 1:
            r = random.randint(1, 6)
            if r == 1:
                gracz.hp -= 1
                print("Straciłeś 1 punkt życia\n")
                smierc.czy_smierc(gracz)
                return
            elif r == 2 or r == 3:
                print("Nic się nie wydarzyło\n")
                return
            elif r == 4 or r == 5:
                if gracz.hp <= gracz.max_hp - 2:
                    gracz.hp += 2
                    print("Odzyskałeś 2 punkty życia\n")
                elif gracz.hp <= gracz.max_hp - 1:
                    gracz.hp += 1
                    print("Odzyskałeś 1 punkt życia\n")
                else:
                    print("Odzyskałeś 0 punktów życia\n")
                return
            elif r == 6:
                gracz.hp = gracz.max_hp
                print("Odzyskałeś punkty życia do maksymalnej wartości!\n")
                return
        elif wybor.isdigit() and int(wybor) == 2:
            print("Idziesz dalej\n")
            return
        else:
            print("Niepoprawny wybór!\n")
