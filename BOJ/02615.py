import sys

input = sys.stdin.readline

def main():
    # 오목판을 입력 받음
    omok = [list(map(int, input().rstrip().split())) for _ in range(19)]
    
    # 방향 정의 (우, 하, 우하단, 좌하단)
    directions = [
        (1, 0),  # 오른쪽
        (0, 1),  # 아래쪽
        (1, 1),  # 오른쪽 아래 대각선
        (-1, 1)  # 왼쪽 아래 대각선
    ]
    
    for x in range(19):
        for y in range(19):
            if omok[x][y] == 0:
                continue
            
            current_stone = omok[x][y]  # 현재 돌의 색상
            
            for dx, dy in directions:
                count = 1
                
                # 현재 방향으로 5개까지 돌이 연속되는지 확인
                for i in range(1, 5):
                    nx, ny = x + dx * i, y + dy * i
                    if 0 <= nx < 19 and 0 <= ny < 19 and omok[nx][ny] == current_stone:
                        count += 1
                    else:
                        break
                
                # 딱 5개가 연속인지 확인 (양 끝에 같은 돌이 더 있는지 확인)
                if count == 5:
                    # 이전 돌이 범위 내에 있고 같은 색이면 승리가 아님 (6목 방지)
                    prev_x, prev_y = x - dx, y - dy
                    if 0 <= prev_x < 19 and 0 <= prev_y < 19 and omok[prev_x][prev_y] == current_stone:
                        continue
                    
                    next_x, next_y = x + dx * 5, y + dy * 5
                    if 0 <= next_x < 19 and 0 <= next_y < 19 and omok[next_x][next_y] == current_stone:
                        continue
                    
                    # 승리한 돌과 좌표 출력
                    print(current_stone)
                    print(x + 1, y + 1)
                    return
    
    # 승부가 나지 않으면 0 출력
    print(0)

if __name__ == "__main__":
    main()
