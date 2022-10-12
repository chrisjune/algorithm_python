n = int(input())
peoples = map(int, input().split())
peoples = sorted(peoples, reverse=True)

count = 0
while peoples:
    first = peoples[0]
    peoples = peoples[first:]
    # for _ in range(first):
    #     peoples.pop(0)
    count += 1

print(count)
