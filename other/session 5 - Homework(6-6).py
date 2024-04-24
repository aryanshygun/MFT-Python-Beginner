# https://quera.org/problemset/108665

vowels = ['a','e','i','o','u']
word = input()

if len(word) == 6:
    vowels_qty=0
    for x in word:
        if x in vowels:
            vowels_qty +=1
    possible = 2**vowels_qty
    print(possible)
# else:
#     print("Error! enter 6 letters")
    
