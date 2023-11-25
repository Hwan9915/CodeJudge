# silver
# solved.ac
# 절사평균 30 : 위 15%, 아래 15%

import sys
from math import ceil, floor

def custom_round(num):
    if num % 1 >= 0.5:
        return int(ceil(num))
    else:
        return int(floor(num))

def main():
    n = int(input())
    lst = []
    for _ in range(n):
        tmp = int(input())
        lst.append(tmp)

    k = int(custom_round(n * 0.15))
    lst.sort()

    if n == 0:
        print(0)
    else:
        print(int(custom_round(sum(lst[k:n-k])/(n-2*k))))



if __name__ == "__main__":
    input = sys.stdin.readline
    main()