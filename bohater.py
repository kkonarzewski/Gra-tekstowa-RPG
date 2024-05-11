bronie = {"brak": 0, "sztylet": 1, "miecz": 2, "topór": 3}


class Bohater:
    def __init__(self, hp=10, atak=5, pieniadze=2, bron="brak", exp=0, poziom=1):
        self.hp = hp
        self.atak = atak
        self.pieniadze = pieniadze
        self.bron = bron
        self.exp = exp
        self.poziom = poziom
