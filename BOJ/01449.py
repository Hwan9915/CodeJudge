# silver
# 수리공 항승
import sys


def main():
    n, l = map(int, input().split())
    hole = list(map(int, input().split()))
    hole.sort()

    ans = 1
    start = hole[0]
    for location in hole[1:]:
        if location in range(start,start+l):
            continue
        else:
            start = location
            ans += 1

    return ans

if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())
