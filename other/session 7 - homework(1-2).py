def calc(a, b):
    answer = a*b - (a + b)
    # print(answer)
    return answer

a, b = map(int, input().split())
c = calc(a, b)
print(c)