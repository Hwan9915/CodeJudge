# silver 4
# 저지
import sys

input = sys.stdin.readline

j = int(input())
a = int(input())

judge = [input().rstrip() for _ in range(j)]

player = [input().rstrip().split() for _ in range(a)]
answer = 0

for i in player:
    size = i[0]
    index = int(i[1]) - 1
    if judge[index] != -1:
        if size == 'S':
            answer += 1
            judge[index] = -1
        elif size == 'M' and (judge[index] == 'M' or judge[index] == 'L'):
            answer += 1
            judge[index] = -1
        elif size == 'L' and judge[index] == 'L':
            answer += 1
            judge[index] = -1
print(answer)
