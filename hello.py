from itertools import combinations

inventory = {
    'r': ('Винтовка', 3, 25),
    'p': ('Пистолет', 2, 15),
    'a': ('Боекомплект', 2, 15),
    'm': ('Аптечка', 2, 20),
    'i': ('Ингалятор', 1, 5),
    'k': ('Нож', 1, 15),
    'x': ('Топор', 3, 20),
    't': ('Оберег', 1, 25),
    'f': ('Фляжка', 1, 15),
    'd': ('Антидот', 1, 10),
    's': ('Еда', 2, 20),
    'c': ('Арбалет', 2, 20)
}


max_cells = 7


valid_combinations = []
for r in range(1, len(inventory) + 1):
    for combo in combinations(inventory.keys(), r):
        total_space = sum(inventory[item][1] for item in combo)
        total_survival_points = sum(inventory[item][2] for item in combo)
        if total_space <= max_cells and total_survival_points > 0:
            valid_combinations.append(combo)


for i, combo in enumerate(valid_combinations, 1):
    print(f"Комбинация {i}: {combo}")