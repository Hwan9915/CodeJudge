import sys

input = sys.stdin.readline

def dfs(depth, start, visited, n, m, char_lst):
    if depth == n:
        ans = ''
        for idx, v in enumerate(visited):
            if v:
                ans += char_lst[idx]
        
        vowels = set('aeiou')
        consonants = set('bcdfghjklmnpqrstvwxyz')
        
        if set(ans) & vowels and sum(1 for char in ans if char in consonants) >= 2:
            print(ans)
        return
    for i in range(start, m):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1, visited, n, m, char_lst)
            visited[i] = False


def main():
    n, m = map(int, input().rstrip().split())
    char_lst = sorted(list(input().rstrip().split()))
    visited = [False] * m
    dfs(0, 0, visited, n, m, char_lst)
    
    
    
if __name__ == "__main__":
    main()