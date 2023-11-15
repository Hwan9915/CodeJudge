# bronze
# 지각

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    for _ in range(n):
        s = int(input())
        t = int(s**0.5)
        while ( t + t**2) > s:
            t -= 1
        print(t)
if __name__ =='__main__':
    main()