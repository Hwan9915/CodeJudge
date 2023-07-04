from collections import deque


def solution(maps):
    # str -> list
    maps_list = [list(s) for s in maps]


    answer = []
    deq = deque()
    n = len(maps_list)
    m = len(maps_list[0])

    for i in range(n):
        for j in range(m):
            if maps_list[i][j] == 'X':
                continue
            else:
                # BFS
                deq.append((i, j))
                matrix_sum = 0
                while deq:
                    x, y = deq.popleft()
                    if maps_list[x][y] == 'X':
                        continue

                    # 섬 크기 더하기
                    matrix_sum = matrix_sum + int(maps_list[x][y])
                    maps_list[x][y] = 'X'

                    dx = [0, 0, 1, -1]
                    dy = [-1, 1, 0, 0]

                    # 상, 하, 좌, 우 탐색
                    for l in range(4):
                        nx = x + dx[l]
                        ny = y + dy[l]
                        if 0 <= nx < n and 0 <= ny < m and maps_list[nx][ny] != 'X':
                            deq.append((nx, ny))

                # 탐색이 끝나면 answer 추가
                answer.append(matrix_sum)

    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)
