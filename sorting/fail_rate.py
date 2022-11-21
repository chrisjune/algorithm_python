n = int(input())
stages = list(map(int, input().split()))

answer = []
length = len(stages)
counts = [0] * length
for s in stages:
    counts[s] += 1

for i in range(1, n + 1):
    count = counts[i]

    fail = 0 if length == 0 else count / length
    answer.append((i, fail))
    length -= count
answer.sort(key=lambda x: x[1], reverse=True)
answer = [i[0] for i in answer]
print(answer)
