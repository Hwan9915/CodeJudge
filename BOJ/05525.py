# silver
# IOIOI

import sys

def main():
    n = int(input())
    len_io = int(input())
    io = input().rstrip()
    ans, cnt, idx = 0, 0, 0

    while idx < len_io - 1:
        if io[idx: idx + 3] == "IOI":
            idx += 2
            cnt += 1
            if cnt == n:
                cnt -= 1
                ans += 1
        else:
            idx += 1
            cnt = 0
    print(ans)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()