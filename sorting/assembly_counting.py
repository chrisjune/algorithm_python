n = input()
targets = [0] * 1000001
for i in input().split():
    targets[int(i)] = 1

m = input()
sources = list(map(int, input().split()))

for source in sources:
    if targets[source]:
        print('yes', end=' ')
    else:
        print('no', end=' ')

