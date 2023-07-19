# silver 1
# 11052번, 카드 구매하기
import sys

N = int(input())

card = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0] * (N+1)

for i in range(N):
    dp[i+1] = card[i]

for i in range(2, N+1):
    for j in range(i, i//2 +1):
        dp[j] = max(dp[j], dp[j-i] + dp[i])

print(dp[N])