# bronze
# 유니대전 퀴즈쇼

import sys

n, m = input().rstrip().split()
n = int(n)
lst = []


for _ in range(n):
    a, b = input().rstrip().split()
    lst.append((a,b))

idx = -1
for i in range(n):
    if lst[i][0] == m:
        idx = i
        break

ans = 0
for i in range(idx):
    if lst[i][1] == lst[idx][1]:
        ans += 1

print(ans)