# 0:00:00 ~ N:59:59

n = int(input())

count = 0
for i in range(0, n+1):
    for j in range(0, 60):
        for k in range(0, 60):
            t = str(i) + str(j) + str(k)
            if "3" in t:
                count += 1

print(count)
