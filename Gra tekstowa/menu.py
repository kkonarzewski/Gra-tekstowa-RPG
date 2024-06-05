import gra
import instrukcja
import wyniki


def menu():
    while 1:
        opcja = input("\nWYBIERZ OPCJĘ W MENU: \n"
                      "1. Rozpocznij grę\n"
                      "2. Instrukcja\n"
                      "3. Wyniki\n"
                      "q. Wyjście\n")
        if opcja.isdigit() and int(opcja) == 1:
            gra.gra()
        elif opcja.isdigit() and int(opcja) == 2:
            instrukcja.instrukcja()
        elif opcja.isdigit() and int(opcja) == 3:
            wyniki.wyniki()
        elif opcja == 'q':
            exit()
        else:
            print("Niepoprawny wybór!\n")


menu()
