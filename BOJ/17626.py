# silver
# Four Squares

import sys
input = sys.stdin.readline
INF = 10000

def main():
    n = int(input())
    ans = [INF] * (n+1)
    for i in range(1,n+1):
        if i ** 0.5 == int(i**0.5):
            ans[i] = 1
        else:
            for j in range(1,int(i**0.5)+1):
                if j**2 < i:
                    if ans[i]>ans[i-j**2]+1:
                        ans[i] = ans[i-j**2] + 1
    print(ans[n])
if __name__ =='__main__':
    main()