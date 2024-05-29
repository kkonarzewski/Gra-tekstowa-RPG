def dol():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w dół \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and int(opcja) == 1:
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def gora():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w górę \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and int(opcja) == 1:
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def prawo():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w prawo \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and int(opcja) == 1:
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def lewo():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w lewo \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and int(opcja) == 1:
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def prawo_dol():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w prawo \n"
                      "2. Idź w dół \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and (int(opcja) == 1 or int(opcja) == 2):
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def gora_prawo():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w górę \n"
                      "2. Idź w prawo \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and (int(opcja) == 1 or int(opcja) == 2):
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def gora_lewo():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w górę \n"
                      "2. Idź w lewo \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and (int(opcja) == 1 or int(opcja) == 2):
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def gora_dol():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w górę \n"
                      "2. Idź w dół \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and (int(opcja) == 1 or int(opcja) == 2):
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def prawo_lewo():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w prawo \n"
                      "2. Idź w lewo \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and (int(opcja) == 1 or int(opcja) == 2):
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def dol_lewo():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w dół \n"
                      "2. Idź w lewo \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and (int(opcja) == 1 or int(opcja) == 2):
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def gora_prawo_dol():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w górę \n"
                      "2. Idź w prawo \n"
                      "3. Idź w dół \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and (int(opcja) == 1 or int(opcja) == 2 or int(opcja) == 3):
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def gora_prawo_lewo():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w górę \n"
                      "2. Idź w prawo \n"
                      "3. Idź w lewo \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and (int(opcja) == 1 or int(opcja) == 2 or int(opcja) == 3):
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def prawo_dol_lewo():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w prawo \n"
                      "2. Idź w dół \n"
                      "3. Idź w lewo \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and (int(opcja) == 1 or int(opcja) == 2 or int(opcja) == 3):
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def gora_dol_lewo():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w górę \n"
                      "2. Idź w dół \n"
                      "3. Idź w lewo \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and (int(opcja) == 1 or int(opcja) == 2 or int(opcja) == 3):
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")


def gora_prawo_dol_lewo():
    while 1:
        opcja = input("\nWybierz opcję: \n"
                      "1. Idź w górę \n"
                      "2. Idź w prawo \n"
                      "3. Idź w dół \n"
                      "4. Idź w lewo \n"
                      "q. Wyjście \n")
        if opcja.isdigit() and (int(opcja) == 1 or int(opcja) == 2 or int(opcja) == 3 or int(opcja) == 4):
            return opcja
        elif opcja == 'q':
            return -1
        else:
            print("Niepoprawna opcja!")
