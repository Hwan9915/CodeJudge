# silver 1
# 15989번, 1, 2, 3 더하기 7
import sys

input=sys.stdin.readline
MAX = 1001
MOD = 1000000009

dp = [[0] * MAX for _ in range(MAX)]
dp[1][1] = 1
dp[2][1], dp[2][2] = 1,1
dp[3][1], dp[3][2], dp[3][3] = 1, 2, 1

for i in range(4, MAX):
    for j in range(1, i + 1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % MOD

N = int(input())
for i in range(N):
    n, m = map(int, input().split())
    print(dp[n][m])