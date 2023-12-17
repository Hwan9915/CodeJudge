# gold
# 궁금한 민호
import sys


def main():
    n = int(input())
    load = [[True] * n for _ in range(n)]
    graph = [list(map(int, input().split())) for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or i == k or j == k:
                    continue

                if graph[i][j] == graph[i][k] + graph[k][j]:
                    load[i][j] = False
                elif graph[i][j] > graph[i][k] + graph[k][j]:
                    print(-1)
                    exit()

    ans = 0
    for i in range(n):
        for j in range(n):
            if load[i][j]:
                ans += graph[i][j]

    return ans//2

if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())
