# gold
# 빵집
import sys


def main():
    r, c = map(int, input().rstrip().split())
    visited = [[False] * c for _ in range(r)]
    matrix = [list(input().rstrip()) for _ in range(r)]
    ans = 0
    def dfs(x,y):
        if y == c-1:
            return True
        for dx in [-1, 0, 1]:
            nx = x + dx
            ny = y + 1
            if 0 <= nx < r and 0 <= ny < c:
                if matrix[nx][ny] != 'x' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if dfs(nx, ny):
                        return True
        return False

    for i in range(r):
        if dfs(i,0): ans += 1

    return ans

if __name__ == "__main__":
    input = sys.stdin.readline
    sys.setrecursionlimit(10000)
    print(main())

