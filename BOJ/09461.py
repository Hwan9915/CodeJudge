# silver 3
# 9461번, 파도반 수열

import sys

input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(101)]
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2

for i in range(5,101):
    dp[i] = dp[i-1] + dp[i-5]

for i in range(N):
    temp = int(input())
    print(dp[temp-1])
