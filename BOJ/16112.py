# silver
# 16112번, 5차 전직
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
n_list = sorted(list(map(int,input().split())))
ans = 0
j = 0
for i in range(0,n):
    ans += n_list[i]*j
    if j < k:
        j+= 1

print(ans)