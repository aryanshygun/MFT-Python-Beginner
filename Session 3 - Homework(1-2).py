x = int(input(" Value for the length of the Rectangle:\n"))
y = int(input(" Value for the width of the Rectangle:\n"))
 

for i in range(x):
    for j in range(y):
        if i == 0 or i == x-1 or j == 0 or j == y-1:
            print("_", end =" ")
        else:
            print(" ", end=" ")
    print()
