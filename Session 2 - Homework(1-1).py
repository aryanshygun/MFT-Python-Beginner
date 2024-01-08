# یک برنامه بنویسید که ابتدا یک عدد از کاربر ورودی بگیرد . به تعداد عدد وارد شده بعد از ان از کاربر ورودی بگیرد و در یک لیست ذخیره کند . سپس بعد از ان index های زوج را در یک لیست و index های فرد را در لیستی دیگر ذخیره کنید و نمایش دهید .


num_qty = int(input("How many numbers?\n"))
main_list = []

for i in range(num_qty):
    num_taken = int(input("Type your numbers:\n"))
    main_list.append(num_taken)

list.sort(main_list)

odd_list=[]
even_list=[]

for i in main_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(f"Here are the Odd list:\n{odd_list}")
print(f"& Here are the even list:\n{even_list}")





# # Initialize an empty list to store numbers with GPT
# numbers_list = []

# # Loop to get 10 numbers from the user
# for i in range(10):
#     while True:
#         try:
#             # Get user input and convert it to a float
#             num = float(input(f"Enter number {i + 1}: "))
#             # Append the number to the list
#             numbers_list.append(num)
#             # Break the loop if input is successful
#             break
#         except ValueError:
#             # Handle the case when the input is not a valid number
#             print("Invalid input. Please enter a valid number.")

# # Display the list of numbers
# print("List of numbers:", numbers_list)