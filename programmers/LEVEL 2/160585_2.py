def tic_tac_toe(board_list):
    tic_o = 0
    if board_list[0] == ['O', 'O', 'O'] or board_list[1] == ['O', 'O', 'O'] or board_list[2] == ['O', 'O', 'O']:
        tic_o += 1

    if board_list[0][0] == 'O' and board_list[1][0] == 'O' and board_list[2][0] == 'O':
        tic_o += 1
    elif board_list[0][1] == 'O' and board_list[1][1] == 'O' and board_list[2][1] == 'O':
        tic_o += 1
    elif board_list[0][2] == 'O' and board_list[1][2] == 'O' and board_list[2][2] == 'O':
        tic_o += 1

    if board_list[0][0] == 'O' and board_list[1][1] == 'O' and board_list[2][2] == 'O':
        tic_o += 1
    elif board_list[0][2] == 'O' and board_list[1][1] == 'O' and board_list[2][0] == 'O':
        tic_o += 1

    tic_x = 0
    if board_list[0] == ['X', 'X', 'X'] or board_list[1] == ['X', 'X', 'X'] or board_list[2] == ['X', 'X', 'X']:
        tic_x += 1

    if board_list[0][0] == 'X' and board_list[1][0] == 'X' and board_list[2][0] == 'X':
        tic_x += 1
    elif board_list[0][1] == 'X' and board_list[1][1] == 'X' and board_list[2][1] == 'X':
        tic_x += 1
    elif board_list[0][2] == 'X' and board_list[1][2] == 'X' and board_list[2][2] == 'X':
        tic_x += 1

    if board_list[0][0] == 'X' and board_list[1][1] == 'X' and board_list[2][2] == 'X':
        tic_x += 1
    elif board_list[0][2] == 'X' and board_list[1][1] == 'X' and board_list[2][0] == 'X':
        tic_x += 1

    return tic_o, tic_x


def solution(board):
    board_list = [list(i) for i in board]

    # x, o 개수 세기
    cnt_x, cnt_o = 0, 0
    for i in range(3):
        for j in range(3):
            if board_list[i][j] == 'X':
                cnt_x += 1
            elif board_list[i][j] == 'O':
                cnt_o += 1
            else:
                continue

    # 순서가 어긋난 경우
    if cnt_x > cnt_o or cnt_o > cnt_x + 1:
        return 0

    tic_o, tic_x = tic_tac_toe(board_list)

    # o 가 완성되었는데 x를 놓은 경우
    if tic_o == 1 and (cnt_x == cnt_o):
        return 0

    # x 가 완성되었는데 o를 놓은 경우
    if tic_x == 1 and (cnt_o > cnt_x):
        return 0


    answer = 1
    return answer