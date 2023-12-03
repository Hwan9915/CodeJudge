# silver
# 20364
import sys


def main():
    n, m = map(int, input().rstrip().split())
    num = []
    vis = set()
    for _ in range(m):
        a = int(input())
        num.append(a)

    def visit(a):
        ans = 0
        b = a
        while b > 0:
            if b in vis:
                ans = b
            b //= 2
        if ans == 0:
            vis.add(a)
        print(ans)

    for i in num:
        visit(i)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
