# gold
# 창영이와 커피
import sys

input = sys.stdin.readline
INF = sys.maxsize
n, c = map(int , input().split())

dp = [INF] * (c + 1)
dp[0] = 0
data = list(map(int, input().split()))

for i in range(n):
    for j in range(c-data[i],-1,-1):
        if dp[j] != INF:
            dp[j+data[i]] =min(dp[j+data[i]], dp[j] + 1)
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])