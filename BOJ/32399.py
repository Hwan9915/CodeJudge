import sys

input = sys.stdin.readline


def main():
    ans = 0
    
    s = input().rstrip()
    if s == '(1)':
        return 0
    elif s == ')1(':
        return 2
    else:
        return 1
    
    
if __name__ == "__main__":
    print(main())