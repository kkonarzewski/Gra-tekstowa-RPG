klasa = ["Wojownik", "Złodziej", "Kaznodzieja", "Biedak", "Mnich"]


def wstep():
    while 1:
        wybor_klasy = input("Wybierz klasę postaci: \n"
                            "1. Wojownik (zwiększony atak, mniejsze życie)\n"
                            "2. Złodziej (więcej pieniędzy, mniejszy atak)\n"
                            "3. Kaznodzieja (zwiększone życie, mniejszy atak)\n"
                            "4. Biedak (zwiększony atak i życie, brak pieniędzy)\n"
                            "5. Mnich (zrównoważone statystyki)\n")

        if wybor_klasy.isdigit() and 1 <= int(wybor_klasy) <= 5:
            print(f"Gratulacje! Twoja klasa postaci to {klasa[int(wybor_klasy) - 1]}.")
            return klasa[int(wybor_klasy) - 1]
        else:
            print("Niepoprawna opcja, proszę wybrać jeszcze raz.\n")
