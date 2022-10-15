count = input()
coins = list(map(int, input().split()))

target = 1


for coin in coins:
    if target < coin:
        break
    target += coin
print(target)
