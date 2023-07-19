# silver 2
# 11722번, 가장 긴 감소하는 부분 수열
import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1] * N
for i in range(N):
    for j in range(0,i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))