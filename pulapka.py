import time
import smierc


def pulapka(gracz):
    print("\nOtwierasz drzwi i idziesz dalej. Po kilku krokach słyszysz jak drzwi zamykają się,"
          " a pochodnie gasną. To pułapka!\n")
    time.sleep(1)
    print("Nagle dostajesz strzałą w kolano, ale ledwo idąc znajdujesz wyjście\n")
    time.sleep(1)
    print("Tracisz 2 punkty życia\n")
    gracz.hp -= 2
    smierc.czy_smierc(gracz)
    return
