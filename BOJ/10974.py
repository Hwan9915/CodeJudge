import sys

input = sys.stdin.readline

def dfs(depth, n, ans):
    if len(ans) == n:
        print(' '.join(ans))
        return
    for i in range(1, n+1):
        if str(i) not in ans:
            ans.append(str(i))
            dfs(depth+1, n, ans)
            ans.pop()

def main():
    n = int(input().rstrip())
    dfs(1, n, [])
    
if __name__ == "__main__":
    main()