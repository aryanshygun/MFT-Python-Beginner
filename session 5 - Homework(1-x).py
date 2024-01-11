# #https://quera.org/problemset/209104

# print("\n--------------------------\n")

# # ans[0] = Haj
# # ans[1] = karbala
# # ans[2] = mashti
# ans = input("Enter Y/N\n").lower()

ans = input().lower()

if ans[0] == 'y':
    print("Haji")
elif ans[1] == 'y':
    print("Karbalaee")
elif ans[2] == 'y':
    print("Mashti")
else:
    print("Agha")