# silver
# 경로 찾기
import sys

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1 or (matrix[i][k] == 1 and matrix[k][j] == 1):
                matrix[i][j] = 1

for i in range(N):
    for j in range(N):
        if matrix[i][j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()