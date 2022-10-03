x = int(input())

cache = [0] * (x + 1)

for i in range(2, x + 1):
    candidate = []

    if i - 1 > 0:
        candidate.append(cache[i - 1])
    if i % 2 == 0:
        candidate.append(cache[i // 2])
    if i % 3 == 0:
        candidate.append(cache[i // 3])
    if i % 5 == 0:
        candidate.append(cache[i // 5])
    cache[i] = min(candidate) + 1

print(cache[x])
