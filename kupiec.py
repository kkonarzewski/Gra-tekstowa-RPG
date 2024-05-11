import random


def kupiec(gracz):
    print("\nPrzemierzając korytarz zauważasz światło pochodni. Gdy podchodzisz bliżej, "
          "Twoim oczom ukazuje się przestraszony kupiec.\n"
          "Czy chcesz coś od niego kupić?")
    while 1:
        opcja = input("1. Tak\n"
                      "2. Nie\n")
        if opcja.isdigit() and int(opcja) == 1:
            while 1:
                opcja1 = input("Kupiec proponuje Ci kilka przedmiotów:\n"
                               "1. Sztylet (+1 obrażeń) - 2 monety\n"
                               "2. Miecz (+2 obrażenia) - 4 monety\n"
                               "3. Topór (+3 obrażenia) - 5 monet\n"
                               "4. Fiolka życia (+2 punkty życia) - 3 monety\n"
                               "5. Tajemnicza fiolka - 1 moneta\n")
                if opcja1.isdigit() and int(opcja1) == 1:
                    if gracz.pieniadze >= 2:
                        gracz.pieniadze -= 2
                        gracz.bron = "sztylet"
                        print("Zakupiłeś sztylet")
                        return
                    else:
                        print("Masz niewystarczającą ilość monet na zakup tego przedmiotu")
                elif opcja1.isdigit() and int(opcja1) == 2:
                    if gracz.pieniadze >= 4:
                        gracz.pieniadze -= 4
                        gracz.bron = "miecz"
                        print("Zakupiłeś miecz")
                        return
                    else:
                        print("Masz niewystarczającą ilość monet na zakup tego przedmiotu")
                elif opcja1.isdigit() and int(opcja1) == 3:
                    if gracz.pieniadze >= 5:
                        gracz.pieniadze -= 5
                        gracz.bron = "topór"
                        print("Zakupiłeś topór")
                        return
                    else:
                        print("Masz niewystarczającą ilość monet na zakup tego przedmiotu")
                elif opcja1.isdigit() and int(opcja1) == 4:
                    if gracz.pieniadze >= 3:
                        gracz.pieniadze -= 3
                        gracz.hp += 2
                        print("Zakupiłeś fiolkę życia")
                        return
                    else:
                        print("Masz niewystarczającą ilość monet na zakup tego przedmiotu")
                elif opcja1.isdigit() and int(opcja1) == 5:
                    if gracz.pieniadze >= 1:
                        gracz.pieniadze -= 1
                        wynik = random.randint(1, 6)
                        if wynik == 1:
                            gracz.hp -= 2
                            print("Zakupiłeś tajemniczą fiolkę - tracisz 2 punkty życia")
                        elif wynik == 2:
                            gracz.hp -= 1
                            print("Zakupiłeś tajemniczą fiolkę - tracisz 1 punkt życia")
                        elif wynik == 3:
                            gracz.hp += 1
                            print("Zakupiłeś tajemniczą fiolkę - zyskujesz 1 punkt życia")
                        elif wynik == 4:
                            gracz.atak += 1
                            print("Zakupiłeś tajemniczą fiolkę - zyskujesz 1 punkt obrażeń")
                        elif wynik == 5:
                            gracz.hp += 2
                            print("Zakupiłeś tajemniczą fiolkę - zyskujesz 2 punkty życia")
                        elif wynik == 6:
                            gracz.atak += 2
                            print("Zakupiłeś tajemniczą fiolkę - zyskujesz 2 punkty obrażeń")
                        return
                    else:
                        print("Masz niewystarczającą ilość monet na zakup tego przedmiotu")
                else:
                    print("Niepoprawny wybór!")
        elif opcja.isdigit() and int(opcja) == 2:
            print("Nie jesteś zainteresowany i idziesz dalej")
            return
        else:
            print("Niepoprawny wybór!")
