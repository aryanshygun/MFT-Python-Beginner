#برنامه ای بنویسید که طول و عرض یک مستطیل را گرفته و در خروجی یک مستطیل تو خالی با ورودی های داده شده رسم کند 

x = int(input(" Value for the length of the Rectangle:\n"))
y = int(input(" Value for the width of the Rectangle:\n"))
 

for i in range(x):
    for j in range(y):
        if i == 0 or i == x-1 or j == 0 or j == y-1:
            print("_", end =" ")
        else:
            print(" ", end=" ")
    print()



print('\n')


############# hollow square
z = int(input(" Value for the sides of the square:\n"))

for i in range(z):
    if i == 0 or i == z-1:
        print("* "*z)
    else:
        print("* " + "  "*(z-2) +"*")