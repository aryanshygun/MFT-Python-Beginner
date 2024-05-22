#  برنامه ای بنویسید که عددی از کاربر گرفته و تشخیص دهد که آیا پالیدروم است یا خیر

print("\n--------------------------\n")

num = input('Enter a num:\n')
num_check= str(num)

if num == int(num_check[::-1]):
    print('num is Palindrome')
else:
    print('num isnt Palindrome')