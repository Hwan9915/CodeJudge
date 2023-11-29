# gold
# 리모컨
import sys

def main():
    N = int(input())
    ans = abs(100 - N)  
    M = int(input())
    
    if M:  
        broken = set(input().split())
    else:
        broken = set()

    for num in range(1000001):
        for N in str(num):
            if N in broken:  
                break
        else:  
            if ans > len(str(num)) + abs(num - N):
                ans = len(str(num)) + abs(num - N)

    print(ans)



if __name__ == '__main__':
    input = sys.stdin.readline
    main()