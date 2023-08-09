# gold
# 적록색약
import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
rgb_matrix = [list(input().rstrip()) for _ in range(N)]
rb_matrix = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if rgb_matrix[i][j] == 'G':
            rb_matrix[i].append('R')
        else:
            rb_matrix[i].append(rgb_matrix[i][j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def rgb_bfs(x, y, color):
    queue = deque()
    queue.append((x, y))
    rgb_matrix[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not 0 <= nx < N or not 0 <= ny < N:
                continue
            if color == rgb_matrix[nx][ny]:
                queue.append((nx, ny))
                rgb_matrix[nx][ny] = 0

def rb_bfs(x, y, color):
    queue = deque()
    queue.append((x, y))
    rb_matrix[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not 0 <= nx < N or not 0 <= ny < N:
                continue
            if color == rb_matrix[nx][ny]:
                queue.append((nx, ny))
                rb_matrix[nx][ny] = 0

rgb_cnt = 0
for i in range(N):
    for j in range(N):
        if rgb_matrix[i][j] != 0:
            rgb_cnt += 1
            rgb_bfs(i, j, rgb_matrix[i][j])

rb_cnt = 0
for i in range(N):
    for j in range(N):
        if rb_matrix[i][j] != 0:
            rb_cnt += 1
            rb_bfs(i, j, rb_matrix[i][j])

print(rgb_cnt,rb_cnt)