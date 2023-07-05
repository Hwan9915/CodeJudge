import sys

input = sys.stdin.readline

dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 3

N = int(input())

for i in range(3, N+1):
    dp[i] = (dp[i-1] +2 * dp[i-2]) % 10007

print(dp[N])