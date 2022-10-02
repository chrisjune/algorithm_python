x = int(input())

cache = [0] * 30001
for i in range(2, x + 1):
    # 1 뺀경우
    cache[i] = cache[i - 1] + 1
    # 2. 나눈경우
    if cache[i] % 2 == 0:
        cache[i] = min(cache[i], cache[i // 2] + 1)

    if cache[i] % 3 == 0:
        cache[i] = min(cache[i], cache[i // 3] + 1)

    if cache[i] % 5 == 0:
        cache[i] = min(cache[i], cache[i // 5] + 1)
print(cache[x])
