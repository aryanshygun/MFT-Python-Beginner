# https://quera.org/problemset/2794?tab=description

print("\n--------------------------\n")
coords_list = []
coords_num = 3
coords_entered = 0

for x in range(coords_num):
    coords = input("Enter your coords with 1 space in between: "
                f"({coords_num-coords_entered} coords remaining.)\n")

    coords = list(map(int, coords.split()))
    coords_list.append(coords)
    coords_entered += 1

print()

print(f"the original list: {coords_list}")

print()

x1, y1 = coords_list[0]
x2, y2 = coords_list[1]
x3, y3 = coords_list[2]

print(f"x1, y1: {x1}, {y1}")
print(f"x2, y2: {x2}, {y2}")
print(f"x3, y3: {x3}, {y3}")

print()

import math

if x1 == x2:
    delta = int(math.fabs(y1 - y2))
    x4 = x3
    if y3 == max(y1, y2):
        y4 = int(math.fabs(y3 - delta))
    else:
        y4 = int(math.fabs(y3 + delta))
    print(f"coords of the 4th point is:\nx4, y4: {x4}, {y4}")

elif x2 == x3:
    delta = int(math.fabs(y2 - y3))
    x4 = x1
    if y1 == max(y2, y3):
        y4 = int(math.fabs(y1 - delta))
    else:
        y4 = int(math.fabs(y1 + delta))
    print(f"coords of the 4th point is:\nx4, y4: {x4}, {y4}")

elif x1 == x3:
    delta = int(math.fabs(y1 - y3))
    x4 = x2
    if y2 == max(y1, y3):
        y4 = int(math.fabs(y2 - delta))
    else:
        y4 = int(math.fabs(y2 + delta))
    print(f"coords of the 4th point is:\nx4, y4: {x4}, {y4}")
