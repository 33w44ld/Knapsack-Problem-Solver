def run_dynamic_programming(current_data):
    C, n, items = current_data
    
    dp = [[0] * (C + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        p, w = items[i - 1]  
        for j in range(C + 1):
            if w <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + p)
            else:
                dp[i][j] = dp[i - 1][j]
                
    best_value = dp[n][C]
    
    best_combination = []
    j = C
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            best_combination.append(i)  
            p, w = items[i - 1]
            j -= w
            
    best_combination.reverse()

    print("\n--- Wynik Programowania Dynamicznego ---")
    print(f"Maksymalna wartość: {best_value}")
    print(f"Wybrane przedmioty (indeksy): {best_combination}")
    print("----------------------------------------")

    return best_value, best_combination