###### Practice num 2


### n = 10

Fibonacci = []

n = int(input("Give me a value for n:\n"))

for i in range(n):
    if i<2:
        Fibonacci.append(i)
    else:
        Fibonacci.append(Fibonacci[-1] + Fibonacci[-2])

for x in Fibonacci:
    print(x, end=" ")