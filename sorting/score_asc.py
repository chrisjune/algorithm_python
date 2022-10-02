counts = int(input())
data = []
for _ in range(counts):
    inputs = input().split()
    data.append((inputs[0], int(inputs[1])))
    data.sort(key=lambda x: x[1])

for i in data:
    print(i[0], end=' ')