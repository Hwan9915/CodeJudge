# silver 2
# 11051번, 이항 계수 2

import sys

dp = [[0]*1001 for _ in range(1001)]
dp[1][0] = 1
dp[1][1] = 1
for i in range(2,1001):
    for j in range(0,i+1):
        if j==0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007

input = sys.stdin.readline

n, k = map(int, input().split())
print(dp[n][k])


