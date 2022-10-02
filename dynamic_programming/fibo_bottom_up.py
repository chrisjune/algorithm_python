cache = [0] * 5001


def fibo_bottom_up(x):
    cache[1] = 1
    cache[2] = 1
    for i in range(3, x+1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[x]


print(fibo_bottom_up(5000))
