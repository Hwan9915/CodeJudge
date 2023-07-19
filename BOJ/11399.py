# silver 4
# 11399번, ATM
import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
arr.sort()
arr_sum = [0] * N
for i in range(N):
    arr_sum[i] = sum(arr[0:i+1])

print(sum(arr_sum))