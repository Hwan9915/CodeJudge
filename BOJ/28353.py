# silver
# 고양이 카페
import sys

input = sys.stdin.readline

answer = 0
n, m = map(int, input().rstrip().split())
arr = sorted(list(map(int,input().rstrip().split())))

i = 0
j = len(arr) - 1
while i < j:
    if arr[i] + arr[j] <= m:
        answer += 1
        i += 1
        j -= 1
    else:
        j -= 1
print(answer)
