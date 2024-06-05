def czy_smierc(gracz):
    if gracz.hp <= 0:
        print("\nZGINĄŁEŚ! KONIEC GRY!\n")
        import menu
        menu.menu()
