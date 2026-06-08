def run_print_action(current_data):
    if current_data:
        C, n, items = current_data
        print(f"\n--- Parametry Plecaka ---")
        print(f"Pojemność maksymalna (C): {C}")
        print(f"Liczba przedmiotów (n): {n}")
        print(f"Lista przedmiotów (wartość, objętość):")
        for idx, (p, w) in enumerate(items, 1):
            print(f"  [{idx}] p = {p}, w = {w}")
        print("-------------------------\n")
    else:
        print("Brak danych do wyświetlenia.")