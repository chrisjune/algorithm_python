count = input()
coins = list(map(int, input().split()))

mem = [1000001] * 1000001
mem[0] = 0
for i in range(1, 1000001):
    candidate = []
    for coin in coins:
        if i - coin >= 0 and i % coin == 0:
            candidate.append(mem[i - coin] + 1)
    mem[i] = min(candidate)
    if mem[i] == 1000001:
        print(i)
        break
print("fin")
