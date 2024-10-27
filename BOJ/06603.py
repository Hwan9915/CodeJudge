import sys

input = sys.stdin.readline

def dfs(depth, start, n, visited, lst):
    if depth == 6:
        ans = []
        for i, v in enumerate(visited):
            if v:
                ans.append(str(lst[i]))
        print(' '.join(ans))
        return
    
    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1, n, visited, lst)
            visited[i] = False
    
def main():
    while True:
        tc = list(map(int, input().rstrip().split()))
        if tc[0] == 0:
            break
        n, lst = tc[0], tc[1:]
        visited = [False] * n
        dfs(0, 0, n, visited, lst)
        print()
        
    
    
if __name__ == "__main__":
    main()