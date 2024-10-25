import sys

input = sys.stdin.readline
mn = 10e7

def dfs(depth, start, m, chicken, chicken_house, visited, house):
    global mn
    # depth, start
    if depth == m:
        chicken_sum = 0
        for x1, y1 in house:
            tmp_mn = 10e7
            for x2, y2 in chicken:
                if tmp_mn > abs(x1-x2) + abs(y1-y2):
                    tmp_mn = abs(x1-x2) + abs(y1-y2)
            chicken_sum += tmp_mn
        mn = min(mn, chicken_sum) 
        return

    # dfs 탐색
    for i in range(start, len(chicken_house)):
        if not visited[i]:
            visited[i] = True
            chicken.append(chicken_house[i])
            dfs(depth+1, i+1, m, chicken, chicken_house, visited, house)
            chicken.pop()
            visited[i] = False

    
    

def main():
    n, m = map(int, input().rstrip().split())
    chicken_map = [list(map(int, input().rstrip().split())) for _ in range(n)]
    chicken_house, house = [], []
    
    for i in range(n):
        for j in range(n):
            if chicken_map[i][j] == 1:
                house.append((i, j))
            elif chicken_map[i][j] == 2:
                chicken_house.append((i, j))
    
    chicken = []
    visited = [False] * len(chicken_house)
    dfs(0, 0, m, chicken, chicken_house, visited, house)
    
    
if __name__ == "__main__":
    main()
    print(mn)