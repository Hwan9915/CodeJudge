# silver 2
# 11053번, 가장 긴 증가하는 부분 수열
import sys

N = int(input())

array = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [1] * N

for i in range(N):
    for j in range(0,i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))