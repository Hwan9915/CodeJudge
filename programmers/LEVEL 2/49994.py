def solution(dirs):
    answer = 0
    direct = {'U':(0, 1), 'D':(0, -1), 'R':(1, 0), 'L':(-1, 0)}
    ans = set()
    x, y = 0, 0
    for i in dirs:
        dx, dy = direct[i]
        nx, ny = x + dx, y+dy
        if abs(nx) > 5 or abs(ny)> 5:
            continue
        ans.add((x,y,nx,ny))
        ans.add((nx,ny,x,y))
        x, y = nx, ny
    
    return len(ans) // 2    

if __name__ == "__main__":
    print(solution("ULURRDLLU"))