# silver 4
# 10546번, 배부른 마라토너

import sys

input = sys.stdin.readline

N = int(input())

people = dict()

for i in range(N):
    temp = input()
    if temp not in people:
        people[temp] = 1
    else:
        people[temp] += 1

for j in range(N-1):
    temp = input()
    people[temp] -= 1

for i in people:
    if people[i] == 1:
        print(i)
        break
