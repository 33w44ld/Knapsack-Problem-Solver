import random
import os

def generate_knapsack_data(n: int, C: int, filepath: str) -> None:
	dir_name = os.path.dirname(filepath)
	if dir_name: 
		os.makedirs(dir_name, exist_ok=True)

	with open(filepath, 'w', encoding='utf-8') as f:
		f.write(f"{C}\n")
		f.write(f"{n}\n")

		for _ in range(n):
			p = random.randint(1, 100)
			w_max = max(1, C // 2)
			w = random.randint(1, w_max)
			f.write(f"{p} {w}\n")