# silver
# 줄세우기
import sys


def main():
    t = int(input())
    for k in range(t):
        lst = list(map(int, input().rstrip().split()))
        ans = 0
        for i in range(1, 21):
            for j in range(i, 21):
                if lst[i] > lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
                    ans += 1

        print(k+1, ans)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()