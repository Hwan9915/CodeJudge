import sys

input = sys.stdin.readline
mn = 10e7
n = 0
num_array = []
visited = []

def dfs(len_lst, index):
    global mn
    if len_lst == n // 2:
        a, b = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += num_array[i][j]
                elif not visited[i] and not visited[j]:
                    b += num_array[i][j]
        
        mn = min(mn, abs(a - b))
        return
    
    for i in range(index, n):
        if not visited[i]:
            visited[i] = True
            dfs(len_lst + 1, i + 1)
            visited[i] = False

# main 함수 제거, 전체 코드를 본문에 작성
n = int(input().rstrip())
num_array = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [False] * (n + 1)

dfs(0, 0)
print(mn)
