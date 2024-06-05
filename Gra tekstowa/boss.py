import przeciwnik


class BossLatwy(przeciwnik.Przeciwnik):
    def __init__(self, hp, atak):
        super().__init__(hp + 2, atak + 2)


class BossSredni(przeciwnik.Przeciwnik):
    def __init__(self, hp, atak):
        super().__init__(hp + 4, atak + 4)
