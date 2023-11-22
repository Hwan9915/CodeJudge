# bronze
# 6174
import sys

def main():
    n = int(input())
    for _ in range(n):
        kaprekar = int(input())
        cnt = 0
        while kaprekar != 6174:
            a = sorted(list(str(kaprekar)))
            b = list(reversed(a))
            while len(b) < 4:
                b.append('0')
            kaprekar =  int(''.join(b)) - int(''.join(a))
            cnt += 1

        print(cnt)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()