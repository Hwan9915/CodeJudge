# silver 1
# 카드 구매하기 2
import sys

INF = sys.maxsize

input = sys.stdin.readline

n = int(input())

cards = [0] + list(map(int,input().split()))
dp = [0] * (n+1)



for i in range(1, n+1):
    for j in range(1, i + 1):
        if dp[i] == 0:
            dp[i] = dp[i-j] + cards[j]
        else:
            dp[i] = min(dp[i], dp[i-j] + cards[j])

print(dp[n])