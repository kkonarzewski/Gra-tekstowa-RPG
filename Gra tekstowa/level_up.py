def level_up(gracz):
    gracz.poziom += 1
    gracz.exp -= 10 + (gracz.poziom - 2) * 2
    print(f"\nGratulacje! Zdobywasz {gracz.poziom} poziom\n")
    while 1:
        wybor = input("Co chcesz ulepszyć?\n"
                      "1. +1 punkt obrażeń\n"
                      "2. +1 punkt maksymalnego życia\n")
        if wybor.isdigit() and int(wybor) == 1:
            gracz.atak += 1
            break
        elif wybor.isdigit() and int(wybor) == 2:
            gracz.hp += 1
            gracz.max_hp += 1
            break
        else:
            print("Niepoprawny wybór!")
    return
