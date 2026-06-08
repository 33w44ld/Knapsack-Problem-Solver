import os

def load_knapsack_data(filepath: str):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Plik '{filepath} nie istnieje.")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    if len(lines) < 2:
        raise ValueError("Plik jest pusty lub ma zły format.")  
    
    C = int(lines[0].strip())
    n = int(lines[1].strip())

    items = []
    for line in lines[2:2 + n]:
        parts = line.split()
        if len(parts) >= 2:
            p, w = int(parts[0]), int(parts[1])
            items.append((p, w))
    
    return C, n, items