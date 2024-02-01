# https://quera.org/problemset/209103

x, y = list(map(int, input().split()))

def decarty(x, y):
    print("| "*y + "|")
    print(" _"*y)

print(" _"*y)
for j in range(x):
    decarty(x, y)