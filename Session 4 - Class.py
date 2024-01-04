# a = [ "amir","ali","reza"]
# b = [ "babaii","davoodi","asghari"]

# for first_name,last_name in enumerate(zip(a,b)):
#     print(f"{first_name} {last_name}")
#     print("\n")
#     print(first_name+' '+last_name)


  
names = ['amir','ali','reza','kasra','arsalan','aryan']
# names = [chr(random.randint(ord('a'),ord('z'))) for _ in range(10)]

num= int(input(" enter how many?\n"))
odd_list=[]
even_list= []
for num,name in enumerate(names):
    if num % 2 == 0:
        even_list.append((num,name)) 
    else:
        odd_list.append((num,name))

print(even_list)
print(odd_list)


