# gold
# A와 B
import sys


def main():
    s = list(input().rstrip())
    t = list(input().rstrip())
    len_s, len_t = len(s), len(t)

    while len_s != len_t:
        if t[-1] == 'A':
            t.pop()
            len_t -= 1

        elif t[-1] == 'B':
            t.pop()
            len_t -= 1
            t = list(reversed(t))
    if s == t:
        return 1
    else:
        return 0


if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())
