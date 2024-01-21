# silver
# 돌 게임
import sys


def main():
    n = int(input().rstrip())
    if n % 2 == 0:
        return "CY"
    else:
        return "SK"


if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())
