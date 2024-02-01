
x, y, z = map(int, input().split())

matrix1 = []
for i in range(x):
    row_num = input().split()
    row = []
    # if type(row_num) != int:
    #         print("Only enter numbers!\n")
            
    for x in row_num:
        row.append(int(x))
        
    # if len(row) != x:
    #     print("Enter the correct amount of numbers!\n")
    # else:
    #     matrix1.append(row)
    matrix1.append(row)

matrix2 = []
for i in range(y):
    row_num = input().split()
    row = []
    for x in row_num:
        row.append(int(x))
    matrix2.append(row)
    
print("This is the first matrix:")
for row in matrix1:
    print(row)

print("This is the second matrix:")
for row in matrix2:
    print(row)
    
matrix3 = []
for x in range(len(matrix1)):
    row = []
    for y in range(len(matrix2[0])):
        element= 0
        for i in range(len(matrix2)):
            element = matrix1[x][i] * matrix2[i][y] + element
        row.append(element)
    matrix3.append(row)
    
print("This is the third matrix:")
for row in matrix3:
    print(row)