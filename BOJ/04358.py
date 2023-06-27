# silver 2
# 4358번, 생태학

import sys

animals_dict = dict()
animals_num = 0
while True:
    temp = sys.stdin.readline().rstrip()
    if temp == "":
        break
    animals_num += 1
    if temp not in animals_dict:
        animals_dict[temp] = 1
    else:
        animals_dict[temp] += 1

animals = []

for i in animals_dict:
    animals.append((i, animals_dict[i]))

animals = sorted(animals)

for i in animals:
    print(f"{i[0]} {i[1]/animals_num*100:.4f}")
