# silver 2
# 1793번, 타일링

import sys

input = sys.stdin.readline

dp = [0 for _ in range(251)]
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3, 251):
    dp[i] = dp[i-1] + 2 * dp[i-2]

while True:
    try:
        temp = int(input())
        print(dp[temp])
    except:
        break