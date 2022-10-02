cache = [0] * 101
def fibo(x):

    if x == 1 or x == 2:
        return 1

    if cache[x]:
        return cache[x]

    cache[x] = fibo(x-1) + fibo(x-2)
    return cache[x]

print(fibo(100))