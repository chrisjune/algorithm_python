n, m, k = map(int, input().split())
targets = list(map(int, input().split()))
targets.sort()

first = targets[-1]
second = targets[-2]

# 가장 큰수가 곱해지는 개수
count = 0
count += m // (k+1) * k
count += m % (k+1)

total = first * count
total += (m - count) * second

print(total)