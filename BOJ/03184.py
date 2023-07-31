# silver 1
# 3184번, 양
import sys, collections

input = sys.stdin.readline

# 행렬 입력
row, col = map(int, input().rstrip().split())
matrix = [list(input().rstrip()) for _ in range(row)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    wolf, sheep = 0, 0
    deq = collections.deque([])
    deq.append([x,y])
    while deq:
        x, y = deq.popleft()
        if matrix[x][y] == '#':
            continue
        else:
            if matrix[x][y] == 'o':
                sheep += 1
            elif matrix[x][y] == 'v':
                wolf += 1
            matrix[x][y] ='#'
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] != '#':
                    deq.append((nx,ny))
    if wolf >= sheep:
        sheep = 0
    else:
        wolf = 0
    return wolf, sheep

v, o = 0, 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] == '#':
            continue
        else:
            v_temp, o_temp = bfs(i,j)
            v += v_temp
            o += o_temp
print(o,v)
# 비어 있는 필드 찾기
# 늑대와 양의 개수 파악하기
# 결론 내기