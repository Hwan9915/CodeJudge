# silver
# 단지번호 붙이기
import sys
sys.setrecursionlimit(10**6)
from collections import deque

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int,list(input().rstrip()))) for _ in range(N)]

cnt = 0
homes = 0
home = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    global homes
    matrix[x][y] = 0
    homes += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not 0 <= nx <N or not 0 <= ny < N:
            continue
        if matrix[nx][ny] == 0:
            continue
        dfs(nx,ny)




for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            homes = 0
            dfs(i, j)
            home.append(homes)
            cnt += 1

print(cnt)
home.sort()
for i in home:
    print(i)