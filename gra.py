import bohater
import wstep
import latwy
import sredni


def gra():
    wybor_klasy, wybor_mapy = wstep.wstep()

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

    if int(wybor_mapy) == 1:
        latwy.latwy(gracz)
    elif int(wybor_mapy) == 2:
        sredni.sredni(gracz)
