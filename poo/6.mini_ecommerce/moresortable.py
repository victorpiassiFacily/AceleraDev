import random

num_list = {}

for i in range(1000000):
    pt1 = random.randint(0, 99)
    pt2 = random.randint(0, 99)
    pt3 = random.randint(0, 99)

    number = f"{pt1} {pt2} {pt3}"

    if number in num_list:
        num_list[number] += 1

    else:
        num_list[number] = 1

for key, value in num_list.items():
    if value > 6:
        print(key, value)
