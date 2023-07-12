# silver 1
# 15989번, 1, 2, 3 더하기 4
import sys

input=sys.stdin.readline

n = int(input())

dp = [0] * 10001
dp[1], dp[2], dp[3] = 1, 2,3
for i in range(4,10001):
    dp[i] = dp[i-3] + i // 2 + 1
for i in range(n):
    temp = int(input())
    print(dp[temp])