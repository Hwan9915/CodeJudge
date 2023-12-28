# gold
# 주사위
import sys


def main():
    n = int(input())
    tmp_lst = list(map(int, input().rstrip().split()))

    lst = []
    lst.append(min(tmp_lst[0],tmp_lst[5]))
    lst.append(min(tmp_lst[1],tmp_lst[4]))
    lst.append(min(tmp_lst[2],tmp_lst[3]))

    lst.sort()
    ans = 0

    if n == 1:
        return sum(tmp_lst) - max(tmp_lst)
    elif n >= 2:
        # 1면만 보이는 수
        ans += ((n - 2) ** 2 * 5 + (n - 2) * 4) * lst[0]

        # 2면만 보이는 수
        ans += ((n - 2) * 8 + 4) * (lst[1] + lst[0])

        # 3면만 보이는 수
        ans += 4 * (lst[2] + lst[1] + lst[0])

        return ans


if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())
