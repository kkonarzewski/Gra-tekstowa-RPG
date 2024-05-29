def wyniki():
    while 1:
        opcja = input("\nJAKIE WYNIKI CHCESZ ZOBACZYĆ: \n"
                      "1. Poziom łatwy \n"
                      "2. Poziom średni \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and int(opcja) == 1:
            try:
                with open('data/wyniki_latwy.txt', 'r') as f:
                    print(f.read())
            except FileNotFoundError:
                print("\nNie ma jeszcze żadnych wyników dla tego poziomu trudności \n")
        elif opcja.isdigit() and int(opcja) == 2:
            try:
                with open('data/wyniki_sredni.txt', 'r') as f:
                    print(f.read())
            except FileNotFoundError:
                print("\nNie ma jeszcze żadnych wyników dla tego poziomu trudności \n")
        elif opcja == 'q':
            return
        else:
            print("Niepoprawna opcja!\n")
