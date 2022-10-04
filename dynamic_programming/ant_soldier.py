cnt = int(input())
inventory = list(map(int, input().split()))

# a[i] = max(a[i-1], a[i-2] + k)

store = [0] * cnt
store[0] = inventory[0]
store[1] = max(store[0], inventory[1])
for i in range(2, cnt):
    store[i] = max(store[i - 1], store[i - 2] + inventory[i])

print(store[cnt-1])
