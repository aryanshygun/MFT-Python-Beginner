def decor(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} is about to start!')
        x = func(*args, **kwargs)
        print(f'{func.__name__} is finished!')
        return x
    return wrapper

@decor
def prime_check(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True
    
n = int(input())
print(prime_check(n))


