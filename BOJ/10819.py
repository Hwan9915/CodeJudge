import sys

input = sys.stdin.readline
ans = 0

def dfs(depth, n, visited, lst, tmp_lst):
    global ans
    if depth == n:
        total = 0
        for i in range(n-1):
            total += abs(tmp_lst[i] - tmp_lst[i+1])
        ans = max(total, ans)
        return
        
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            tmp_lst.append(lst[i])
            dfs(depth+1, n, visited, lst, tmp_lst)
            tmp_lst.pop()
            visited[i] = False
        
# start의 차이에 대해 알아보자      

def main():
    n = int(input().rstrip())
    lst = list(map(int, input().rstrip().split()))
    visited = [False] * n
    dfs(0, n, visited, lst, [])
    
    return ans
            
    
if __name__ == "__main__":
    print(main())