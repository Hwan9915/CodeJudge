# gold
# 구슬 찾기
import sys


def main():
    n, m = map(int, input().split())
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = True

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    ans = 0

    for i in range(1, n+1):
        l, r = 0, 0
        for j in range(1, n+1):
            if i == j:
                continue
            elif graph[i][j]:
                r += 1
            elif graph[j][i]:
                l += 1
        if l > n//2 or r > n//2:
            ans += 1

    return ans


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = 10e4
    print(main())
