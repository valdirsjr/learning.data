from functools import lru_cache

@lru_cache(maxsize = 10000)
def fibonacci(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_manual_cache(n):
    fibonacci_cache = {}
    # dictionary for cache last results to increase performance
    # if n is cached, return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # cache the new value and return it
    fibonacci_cache[n] = value
    return value


# for i in range(1,181):
#     print(i,":",fibonacci(i))

fibo = [0,1]
for i in range(100):
    fibo.append(fibo[-1]+fibo[-2])
    del fibo[0]

print(fibo)
