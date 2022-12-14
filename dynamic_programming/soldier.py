# cnt = int(input())
# sols = list(map(int, input().split()))

cnt = 7
sols = [15, 11, 4, 8, 5, 2, 4]

sols.reverse()
# 4 2 5 8 4 11 15
dp = [1] * cnt

for i in range(0, cnt):
    for j in range(0, i):
        if sols[j] < sols[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp)
print(cnt - max(dp))
