# silver 3
# 9095번, 1,2,3 더하기

import sys

input=sys.stdin.readline

n = int(input())

dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for i in range(n):
    temp = int(input())
    print(dp[temp])