# gold
# A와 B 2
import sys


def main():
    a = list(input().rstrip())
    b = list(input().rstrip())

    ans = 0

    def num_12919(s):
        if len(s) == len(a):
            if s == a:
                print(1)
                exit()

            return
        if s[-1] == 'A':
            s.pop()
            num_12919(s)
            s.append('A')
        if s[0] == 'B':
            s.reverse()
            s.pop()
            num_12919(s)
            s.append('B')
            s.reverse()

    num_12919(b)
    return ans


if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())
