# silver 3
# 1463번, 1로 만들

import sys

input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N + 1)]

for i in range(2, N + 1):
    if i % 6 == 0:
        dp[i] = min(dp[i // 2], dp[i // 3], dp[i - 1]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i // 2], dp[i - 1]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i // 3], dp[i - 1]) + 1
    else:
        dp[i] = dp[i - 1] + 1

print(dp[N])
