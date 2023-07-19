# silver 4
# 2217번, 로프
import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = [0] * N
for i in range(N):
    arr[i] = int(input().rstrip())
arr.sort()
max_num = -1
for i in range(N):
    arr[i] = arr[i]*(N-i)
    if max_num < arr[i]:
        max_num = arr[i]


sys.stdout.write(str(max_num))