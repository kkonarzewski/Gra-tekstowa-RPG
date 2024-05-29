def instrukcja():
    while 1:
        opcja = input("\nINSTRUKCJA GRY: \n"
                      "1. Cała gra toczy się w terminalu \n"
                      "2. Daną opcję wybiera się poprzez naciśnięcie odpowiedniej cyfry, a następnie naciśnięcie "
                      "przycisku ENTER \n"
                      "3. Wyjście z gry odbywa się poprzez naciśnięcie klawisza \'q\' w odpowiednich momentach \n"
                      "4. Wyniki zapisywane są wyłącznie podczas dostępu do internetu \n"
                      "\nNaciśnij \'q\' aby powrócić do menu \n")
        if opcja == 'q':
            return
