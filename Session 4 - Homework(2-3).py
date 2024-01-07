# برنامه ای بنویسید که یک عدد از کاربر گرفته و اول بودن (prime) یا نبودن آن عدد را چک کند 

print("\n--------------------------\n")

num = input('Type a number:\n')
perfect_divides=0

for i in range(1,num+1):
    if num % i == 0:
        perfect_divides += 1

if perfect_divides == 2:
    print("This number is a Prime.")
else:
    print("This number is not a Prime.")