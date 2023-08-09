# silver
# 음식물 피하기
import sys

input = sys.stdin.readline

N = int(input())
max_num = -1

matrix = []
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    max_num = max(max_num, max(tmp))
    matrix.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [(x, y)]
    matrix_tmp[x][y] = 0
    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < N) and (matrix_tmp[nx][ny] > 0):
                queue.append((nx, ny))
                matrix_tmp[nx][ny] = 0


max_area = 1

for height in range(1, max_num):

    matrix_tmp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_tmp[i][j] = matrix[i][j] - height

    cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix_tmp[i][j] > 0:
                bfs(i, j)
                cnt += 1

    max_area = max(max_area, cnt)

print(max_area)
