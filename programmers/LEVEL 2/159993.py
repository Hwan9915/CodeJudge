from collections import deque

INF = float('inf')


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    matrix = [[INF] * m for _ in range(n)]
    deq = deque()

    # S 위치 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                matrix[i][j] = 0
                deq.append((i, j, 0))
                break
        if deq:
            break

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # S => L
    while deq:
        x, y, cnt = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X':

                # L을 찾았을 경우
                if maps[nx][ny] == 'L':
                    answer += cnt + 1

                    # deq 초기화
                    deq = deque()
                    deq.append((nx, ny, 0))
                    break

                if cnt + 1 < matrix[nx][ny]:
                    matrix[nx][ny] = cnt + 1
                    deq.append((nx, ny, cnt + 1))
        if answer != 0:
            break

    temp_answer = answer
    matrix = [[INF] * m for _ in range(n)]

    # L => E

    while deq:
        x, y, cnt = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X':
                if maps[nx][ny] == 'E':
                    answer += cnt + 1
                    break
                if cnt + 1 < matrix[nx][ny]:
                    matrix[nx][ny] = cnt + 1
                    deq.append((nx, ny, cnt + 1))

        # answer 값이 변하면 break
        if answer != temp_answer:
            break

    # L -> E 경로가 없으면 -1
    if answer == temp_answer:
        return -1

    return answer