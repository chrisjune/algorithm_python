n, k = map(int, input().split())

remain = n
count = 0

while remain > 1:
    if remain % k != 0:
        remain -= 1
        count += 1
        continue
    else:
        remain /= k
        count += 1
print(count)