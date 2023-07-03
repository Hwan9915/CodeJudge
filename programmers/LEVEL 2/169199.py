from collections import deque


def solution(board):
    answer = 0
    N, M = len(board), len(board[0])
    deq = deque()
    matrix = [[999999999] * M for _ in range(N)]

    # R, G 찾기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                deq.append((i, j, 0))
                matrix[i][j] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while deq:
        x, y, cnt = deq.popleft()

        if board[x][y] == 'G':
            return cnt

        for i in range(4):
            nx = x
            ny = y

            while 0 <= nx + dx[i] < N and 0 <= ny + dy[i] < M and board[nx + dx[i]][ny + dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]

            if matrix[nx][ny] > cnt + 1:
                matrix[nx][ny] = cnt + 1
                deq.append((nx, ny, cnt + 1))

    return -1
