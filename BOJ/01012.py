# silver
# 유기농 배추
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

tc = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    matrix[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not 0 <= nx < M or not 0 <= ny < N:
            continue
        if matrix[nx][ny] == 1:
            dfs(nx,ny)




for __ in range(tc):
    N, M, K = map(int, input().split())
    matrix = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        b, a = map(int, input().split())
        matrix[a][b] = 1

    cnt = 0

    for i in range(M):
        for j in range(N):
            if matrix[i][j] != 0:
                cnt += 1
                dfs(i, j)

    print(cnt)
