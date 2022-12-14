table = [
    [3, 10],
    [5, 20],
    [1, 10],
    [1, 20],
    [2, 15],
    [4, 40],
    [2, 200],
]

n = 7
dp = [0] * (n + 1)

# dp[i] = i번째로 부터 마지막날 까지의 최대이익금액

maxvalue = 0
for i in range(n - 1, -1, -1):
    t = table[i][0]
    p = table[i][1]
    if i + t <= n:
        dp[i] = max(p + dp[i + t], maxvalue)
        maxvalue = dp[i]
    else:
        dp[i] = maxvalue
print(dp)
print(maxvalue)
