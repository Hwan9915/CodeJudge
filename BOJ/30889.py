# bronze
# 좌석 배치도

import sys

def main():
    n = int(input().rstrip())

    matrix = [['.'] * 21 for _ in range(10)]

    for _ in range(n):
        a = input().rstrip()
        b, c = a[0], a[1:]

        matrix[ord(b)-65][int(c)] = 'o'

    for i in range(10):
        for j in range(1,21):
            print(matrix[i][j])
        print("")

if __name__ == "__main__":
    input = sys.stdin.readline
    print = sys.stdout.write
    main()