# bronze
# 별 찍기 - 21
import sys


def main():
    n = int(input())
    if n == 1:
        print("*")
        return
    else:
        for i in range(n*2):
            if i % 2 == 0:
                for j in range(n):
                    if j % 2 == 0:
                        print('*')
                    else:
                        print(' ')
            else:
                for j in range(n):
                    if j % 2 == 0:
                        print(' ')
                    else:
                        print('*')
            print('\n')


if __name__ == "__main__":
    input = sys.stdin.readline
    print = sys.stdout.write
    main()