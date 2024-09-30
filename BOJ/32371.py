def main():
    lst = [list(input()) for _ in range(4)]
    ans = list(input())
    delta = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

    for x in range(1,3):
        for y in range(1,9):
            for dx, dy in delta:
                nx = x + dx
                ny = y + dy

                if lst[nx][ny] not in ans:
                    break
            else:
                return lst[x][y]




if __name__ == "__main__":
    print(main())