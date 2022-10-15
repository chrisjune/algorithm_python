n, m = map(int, input().split())
coins = list(map(int, input().split()))

c = [0] * (m + 1)
for coin in coins:
    c[coin] += 1

remain = n
result = 0

for i in range(1, len(c)):
    remain -= c[i]
    result += c[i] * remain
print(result)
