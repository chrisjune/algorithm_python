from itertools import combinations

n, m = map(int, input().split())

house = []
chicken = []
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

chicken_combi = list(combinations(chicken, m))

total_sum = 987654321
for combi in chicken_combi:
    total = 0
    for h in house:
        min_h_distance = 987654321
        for c in combi:
            distance = abs(c[0] - h[0]) + abs(c[1] - h[1])
            min_h_distance = min(min_h_distance, distance)
        total += min_h_distance
    total_sum = min(total_sum, total)
print(total_sum)
