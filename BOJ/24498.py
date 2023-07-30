# silver 4
# 24498번, blobnom

import sys

input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
ans = a_list[0]
for i in range(0,n):
    if i == 0 or i == n-1:
        ans = max(ans, a_list[i])
    else:
        ans = max(ans, a_list[i] + min(a_list[i-1], a_list[i+1]))

print(ans)