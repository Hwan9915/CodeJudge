def tic_tac_toe(player, board):
    tic = 0

    # row
    for i in range(3):
        if all(player == cell for cell in board[i]):
            tic += 1

    # col
    for j in range(3):
        if all(player == board[i][j] for i in range(3)):
            tic += 1

    # diagonal
    if all(board[i][i] == player for i in range(3)):
        tic += 1
    if all(board[i][2 - i] == player for i in range(3)):
        tic += 1

    return tic


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

    tic_o = tic_tac_toe('O', board)
    tic_x = tic_tac_toe('X', board)

    # o 가 완성된 이후 x를 놓은 경우
    if tic_o == 1 and (cnt_x == cnt_o):
        return 0

    # x 가 완성된 이후 o를 놓은 경우
    if tic_x == 1 and (cnt_o > cnt_x):
        return 0

    return 1
