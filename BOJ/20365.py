# silver 3
# 20365번, 블로그2
import sys

input = sys.stdin.readline

n = int(input().rstrip())

problem = list(input())

b, r = 0, 0
if problem[0] =='B':
    b += 1
else:
    r += 1
for i in range(1,n):
    if problem[i-1] != problem[i]:
        if problem[i] == 'B':
            b += 1
        else:
            r += 1
    else:
        continue

print(min(b,r)+1)