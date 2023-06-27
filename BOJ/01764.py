# silver 4
# 1764번, 듣보잡

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

A = set()
for i in range(N):
    temp = sys.stdin.readline().rstrip()
    A.add(temp)

B = set()
for j in range(M):
    temp = sys.stdin.readline().rstrip()
    B.add(temp)

C = sorted(A & B)
print(len(C))
for i in C:
    print(i)
