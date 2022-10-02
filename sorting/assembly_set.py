n = input()
targets = set(map(int, input().split()))

m = input()
sources = list(map(int, input().split()))

for source in sources:
    if source in targets:
        print('yes', end=' ')
    else:
        print('no', end=' ')

