def add_all(*nums):
    numlist=[]
    final = 0
    for i in nums:
        numlist.append(i)
        final += i
    return final

print(add_all(2,4,6,8,10))