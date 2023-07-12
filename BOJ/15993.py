# silver 1
# 15989번, 1, 2, 3 더하기 7

import sys

input = sys.stdin.readline

MAX = 100_001
MOD = 1_000_000_009

dp = [[0,0] for _ in range(MAX)]
dp[1][0], dp[1][1] = 0,1
dp[2][0], dp[2][1] = 1,1
dp[3][0], dp[3][1] = 2, 2

for i in range(4, MAX):
   dp[i][0] = (dp[i-1][1] + dp[i-2][1] + dp[i-3][1]) % MOD
   dp[i][1] = (dp[i-1][0] + dp[i-2][0] + dp[i-3][0]) % MOD

N = int(input())
for i in range(N):
    n = int(input())
    print(dp[n][1], dp[n][0])