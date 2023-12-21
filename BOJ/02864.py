# bronze
# 5와 6의 차이
import sys


def main():
    a, b = map(str, input().rstrip().split())
    a6 = a.replace('5', '6')
    b6 = b.replace('5', '6')

    a5 = a.replace('6', '5')
    b5 = b.replace('6', '5')

    a = int(a5) + int(b5)
    b = int(a6) + int(b6)
    print(a,b)

if __name__ == "__main__":
    input = sys.stdin.readline
    main()
