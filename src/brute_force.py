def run_brute_force(current_data):
    C, n, items = current_data
    best_value = 0 
    best_combination = []

    total_combinations = 2 ** n

    for i in range(total_combinations):
        current_weight = 0
        current_value = 0
        current_combo = []

        for j in range(n):
            if( i // (2 ** j)) % 2 != 0:
                p, w = items[j]
                current_weight += w
                current_value += p
                current_combo.append(j + 1)
        
        if current_weight <= C and current_value > best_value:
            best_value = current_value
            best_combination = current_combo

    print("\n--- Wynik Brute Force ---")
    print(f"Maksymalna wartość: {best_value}")
    print(f"Wybrane przedmioty (indeksy): {best_combination}")
    print("-------------------------")

    return best_value, best_combination