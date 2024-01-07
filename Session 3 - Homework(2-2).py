
# برنامه ای بنویسید که n را از کابر گرفته و دنباله فیبوناچی را تا n امین عنصر چاپ کند . 
## دنباله فیبوناچی : هر عنصر حاصل مجموع دو عنصر قبل خود میباشد

Fibonacci = []

n = int(input("Give me a value for n:\n"))

for i in range(n):
    if i<2:
        Fibonacci.append(i)
    else:
        Fibonacci.append(Fibonacci[-1] + Fibonacci[-2])

for x in Fibonacci:
    print(x, end=" ")