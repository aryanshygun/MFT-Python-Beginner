def main():
    input = input().split(" ")
    n = int(input[0])
    m = int(input[1])
    array = []
    for i in range(n):
        array.append(list(map(int, input().split(" "))))
    s = 0
    if n >= 3 and m >= 3:
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                x = array[i][j]
                a = x > array[i - 1][j] and x > array[i + 1][j] and x < array[i][j - 1] and x < array[i][j + 1]
                b = x > array[i][j - 1] and x > array[i][j + 1] and x < array[i - 1][j] and x < array[i + 1][j]
                if a or b:
                    s += 1
        print(s)
    else:
        print("0")

if __name__ == "__main__":
    main()

