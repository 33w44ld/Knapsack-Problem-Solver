import time
import csv
import random
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.brute_force import run_brute_force
from src.dynamic_programming import run_dynamic_programming

def run_auto_benchmark():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_csv = os.path.join(current_dir, "benchmark_results.csv")
        
    headers = ["n", "C", "Czas_Brute_Force_s", "Czas_PD_s", "Wynik_Wartosc"]
    
    with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for n in range(5, 26):
            C = n * 10  
            
            items = []
            for _ in range(n):
                p = random.randint(1, 100)
                w_max = max(1, C // 2)
                w = random.randint(1, w_max)
                items.append((p, w))
                
            current_data = (C, n, items)
            
            start_bf = time.perf_counter()
            val_bf, _ = run_brute_force(current_data)
            end_bf = time.perf_counter()
            elapsed_bf = end_bf - start_bf
            
            start_dp = time.perf_counter()
            val_dp, _ = run_dynamic_programming(current_data)
            end_dp = time.perf_counter()
            elapsed_dp = end_dp - start_dp
            
            writer.writerow([n, C, f"{elapsed_bf:.6f}", f"{elapsed_dp:.6f}", val_dp])
            f.flush() 
            
            print(f"[Sukces] Ukończono n={n}, C={C} | BF: {elapsed_bf:.4f}s | PD: {elapsed_dp:.4f}s")

    print("Benchmark zakończony sukcesem!")

if __name__ == "__main__":
    run_auto_benchmark()