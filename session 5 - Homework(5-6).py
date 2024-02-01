# https://quera.org/problemset/655/

qty = int(input())
i=0
movies=[]
while i < qty:
    name = input()
    movies.append(name)
    i+=1
for i in movies:
    print(i.title())