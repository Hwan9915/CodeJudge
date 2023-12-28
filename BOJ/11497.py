# silver
# 통나무 건너뛰기
import sys

def main():
    t = int(input().rstrip())
    for __ in range(t):
        n = int(input().rstrip())
        lst = sorted(list(map(int, input().rstrip().split())))
        print(max([lst[i+2]-lst[i] for i in range(n-2)]))

if __name__ =="__main__":
    input = sys.stdin.readline
    main()