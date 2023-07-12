# silver 1
# 1149번, RGB거리
import sys

input = sys.stdin.readline

N = int(input())
dp=[0,0,0]

for _ in range(N):
    i, j, k = list(map(int,input().split()))
    i = min(dp[1:]) + i
    j = min(dp[0],dp[2]) + j
    k = min(dp[:2]) + k
    dp = [i,j,k]

print(min(dp))