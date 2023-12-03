# silver
# 드럼

import sys
from math import gcd


def main():
    n, m = map(int, input().split())

    # n이 큰 수

    # 최소 공배수 생성
    max_ = n * m // gcd(n, m)

    arr1 = [False] * (max_ + 1)
    arr2 = [False] * (max_ + 1)

    for i in range(0, max_ + 1, max_ // m):
        arr1[i] = True

    for j in range(0, max_ + 1, max_ // n):
        arr2[j] = True

    for i in range(1, max_ + 1):
        if arr1[i] and arr2[i]:
            print(3, end='')
        elif arr1[i] and not arr2[i]:
            print(2, end='')
        elif not arr1[i] and arr2[i]:
            print(1, end='')


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
