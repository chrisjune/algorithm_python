n, m = map(int, input().split())
balls = list(map(int, input().split()))

array = [0] * 11
for i, ball in enumerate(balls):
    array[ball] += 1

result = 0
remain = sum(array)
for i in range(1, len(array)):
    remain -= array[i]
    result += array[i] * remain
print(result)


