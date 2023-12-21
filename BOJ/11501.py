# silver
# 주식
import sys


def main():
    t = int(input().rstrip())
    for __ in range(t):
        n = int(input().rstrip())
        n_lst = list(map(int, input().rstrip().split()))

        ans = 0
        max_ = n_lst[-1]
        for i in n_lst[-2::-1]:
            if max_<= i:
                max_ = i
            else:
               ans += max_ - i

        print(ans)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()