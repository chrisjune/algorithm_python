n, m, k = map(int, input().split())
targets = list(map(int, input().split()))
targets.sort()

cnt = 1
sub_cnt = 0
total = 0
while cnt <= m:
    sub_cnt += 1
    if sub_cnt <= k:
        total += targets[-1]
    else:
        total += targets[-2]
        sub_cnt = 0
    cnt += 1

print(total)

