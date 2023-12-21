# gold
# 센서
import sys


def main():
    n = int(input().rstrip())
    k = int(input().rstrip())
    lst = list(map(int, input().rstrip().split()))
    if n <= k:
        return 0

    lst.sort()

    lst_diff = []
    for i in range(1,n):
        lst_diff.append(lst[i] - lst[i-1])

    lst_diff.sort()
    for i in range(k-1):
        lst_diff.pop()

    return sum(lst_diff)


if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())