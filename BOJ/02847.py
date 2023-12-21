# silver
# 게임을 만든 동준이
import sys

def main():
    n = int(input())
    lst = list(reversed([int(input()) for _ in range(n)]))

    ans = 0
    for i in range(1, n):
        if lst[i] >= lst[i-1]:
            ans += lst[i] - lst[i-1] + 1
            lst[i] = lst[i-1] -1
    return ans

if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())