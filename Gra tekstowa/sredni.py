import bohater
import skrzynia
import kupiec
import pulapka
import walka
import kapliczka_zdrowia
import ruch
import time


def sredni(gracz):
    start = time.time()
    jeden(gracz, start)


def jeden(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    opcja = int(ruch.gora_prawo_dol_lewo())
    if opcja == 1:
        dwa(gracz, start)
    elif opcja == 2:
        szesc(gracz, start)
    elif opcja == 3:
        cztery(gracz, start)
    elif opcja == 4:
        trzy(gracz, start)


def dwa(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    pulapka.pulapka(gracz)
    opcja = int(ruch.prawo_dol())
    if opcja == 1:
        piec(gracz, start)
    elif opcja == 2:
        jeden(gracz, start)


def trzy(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    kupiec.kupiec(gracz)
    print("\nNie możesz iść dalej, musisz zawrócić \n")
    jeden(gracz, start)


def cztery(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    opcja = int(ruch.gora_prawo())
    if opcja == 1:
        jeden(gracz, start)
    elif opcja == 2:
        siedem(gracz, start)


def piec(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    opcja = int(ruch.prawo_dol_lewo())
    if opcja == 1:
        osiem(gracz, start)
    elif opcja == 2:
        szesc(gracz, start)
    elif opcja == 3:
        dwa(gracz, start)


def szesc(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    opcja = int(ruch.gora_dol_lewo())
    if opcja == 1:
        piec(gracz, start)
    elif opcja == 2:
        siedem(gracz, start)
    elif opcja == 3:
        jeden(gracz, start)


def siedem(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    walka.walka_wstep(gracz)
    opcja = int(ruch.gora_prawo_lewo())
    if opcja == 1:
        szesc(gracz, start)
    elif opcja == 2:
        dziesiec(gracz, start)
    elif opcja == 3:
        cztery(gracz, start)


def osiem(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    walka.walka_wstep(gracz)
    opcja = int(ruch.prawo_lewo())
    if opcja == 1:
        jedenascie(gracz, start)
    elif opcja == 2:
        piec(gracz, start)


def dziewiec(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    walka.walka_wstep(gracz, "sredni")
    end = time.time()
    print("\nUdało Ci się pokonać bossa i przejść poziom!\n")
    nazwa = input("Podaj swoją nazwę:\n")
    with open("data/wyniki_sredni.txt", "a") as myfile:
        myfile.write(f"{nazwa} -> Osiągnięty czas: " + "%.2f minut\n" % ((end - start) / 60))
    return


def dziesiec(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    skrzynia.skrzynia(gracz)
    opcja = int(ruch.prawo_lewo())
    if opcja == 1:
        jedenascie(gracz, start)
    elif opcja == 2:
        siedem(gracz, start)


def jedenascie(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    opcja = int(ruch.gora_prawo_dol_lewo())
    if opcja == 1:
        osiem(gracz, start)
    elif opcja == 2:
        dwanascie(gracz, start)
    elif opcja == 3:
        dziesiec(gracz, start)
    elif opcja == 4:
        dziewiec(gracz, start)


def dwanascie(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    kapliczka_zdrowia.kapliczka(gracz)
    print("\nNie możesz iść dalej, musisz zawrócić \n")
    jedenascie(gracz, start)
