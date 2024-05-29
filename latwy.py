import bohater
import skrzynia
import kupiec
import pulapka
import walka
import kapliczka_zdrowia
import ruch
import time


def latwy(gracz):
    start = time.time()
    jeden(gracz, start)


def jeden(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze},"
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    opcja = int(ruch.prawo_dol())
    if opcja == 2:
        dwa(gracz, start)
    elif opcja == 1:
        cztery(gracz, start)


def dwa(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    walka.walka_wstep(gracz)
    print("\nNie możesz iść dalej, musisz zawrócić \n")
    jeden(gracz, start)


def trzy(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    walka.walka_wstep(gracz)
    opcja = int(ruch.prawo_dol())
    if opcja == 1:
        szesc(gracz, start)
    elif opcja == 2:
        cztery(gracz, start)


def cztery(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    opcja = int(ruch.gora_prawo_dol_lewo())
    if opcja == 1:
        trzy(gracz, start)
    elif opcja == 2:
        siedem(gracz, start)
    elif opcja == 3:
        piec(gracz, start)
    elif opcja == 4:
        jeden(gracz, start)


def piec(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    pulapka.pulapka(gracz)
    print("\nNie możesz iść dalej, musisz zawrócić \n")
    cztery(gracz, start)


def szesc(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    opcja = int(ruch.prawo_lewo())
    if opcja == 1:
        dziewiec(gracz, start)
    elif opcja == 2:
        trzy(gracz, start)


def siedem(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    opcja = int(ruch.prawo_dol_lewo())
    if opcja == 1:
        dziewiec(gracz, start)
    elif opcja == 2:
        osiem(gracz, start)
    elif opcja == 3:
        cztery(gracz, start)


def osiem(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    skrzynia.skrzynia(gracz)
    print("\nNie możesz iść dalej, musisz zawrócić \n")
    siedem(gracz, start)


def dziewiec(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    kupiec.kupiec(gracz)
    opcja = int(ruch.gora_prawo_lewo())
    if opcja == 1:
        szesc(gracz, start)
    elif opcja == 2:
        dziesiec(gracz, start)
    elif opcja == 3:
        siedem(gracz, start)


def dziesiec(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    kapliczka_zdrowia.kapliczka(gracz)
    opcja = int(ruch.prawo_lewo())
    if opcja == 1:
        jedenascie(gracz, start)
    elif opcja == 2:
        dziewiec(gracz, start)


def jedenascie(gracz, start):
    print(
        f"\nPunkty życia: {gracz.hp}/{gracz.max_hp}, Zadawane obrażenia: {gracz.atak}, Posiadane monety: {gracz.pieniadze}, "
        f"Posiadana broń: {gracz.bron} (+{bohater.bronie[gracz.bron]} obrażeń), Punkty doświadczenia: "
        f"{gracz.exp}/{10 + (gracz.poziom - 1) * 2}, Poziom: {gracz.poziom}\n\n")
    walka.walka_wstep(gracz, "latwy")
    end = time.time()
    print("\nUdało Ci się pokonać bossa i przejść poziom!\n")
    nazwa = input("Podaj swoją nazwę:\n")
    with open("wyniki_latwy.txt", "a") as myfile:
        myfile.write(f"{nazwa} -> Osiągnięty czas: " + "%.2f minut\n" % ((end - start) / 60))
    return
