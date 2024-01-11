# https://quera.org/problemset/2794?tab=description

coords_list = []
coords_num = 3

for x in range(coords_num):
    coords = input()

    coords = list(map(int, coords.split()))
    coords_list.append(coords)

x1, y1 = coords_list[0]
x2, y2 = coords_list[1]
x3, y3 = coords_list[2]

import math

if x1 == x2:
    delta = int(math.fabs(y1 - y2))
    x4 = x3
    if y3 == max(y1, y2):
        y4 = int(math.fabs(y3 - delta))
    else:
        y4 = int(math.fabs(y3 + delta))
    print(f"{x4} {y4}")

elif x2 == x3:
    delta = int(math.fabs(y2 - y3))
    x4 = x1
    if y1 == max(y2, y3):
        y4 = int(math.fabs(y1 - delta))
    else:
        y4 = int(math.fabs(y1 + delta))
    print(f"{x4} {y4}")

elif x1 == x3:
    delta = int(math.fabs(y1 - y3))
    x4 = x2
    if y2 == max(y1, y3):
        y4 = int(math.fabs(y2 - delta))
    else:
        y4 = int(math.fabs(y2 + delta))
    print(f"{x4} {y4}")

