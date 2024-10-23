import sys

input = sys.stdin.readline


def bfs():
    if m == len(s):
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        bfs()
        s.pop()
        visited[i] = False


n, m = map(int, input().split())

s = []
visited = [False] * (n + 1)
bfs()