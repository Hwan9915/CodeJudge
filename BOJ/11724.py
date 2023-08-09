# silver
# 연결 요소의 개수
import sys
from collections import deque

queue = deque([])
input = sys.stdin.readline

vertex, edge = map(int, input().split())
graph = [[] for _ in range(vertex + 1)]
is_visit = [False for _ in range(vertex + 1)]

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    is_visit[start] = True
    queue.append(start)
    while queue:
        next = queue.popleft()
        for j in graph[next]:
            if not is_visit[j]:
                is_visit[j] = True
                queue.append(j)

cnt = 0
for i in range(1, vertex+1):
    if not is_visit[i]:
        cnt += 1
        bfs(i)

print(cnt)