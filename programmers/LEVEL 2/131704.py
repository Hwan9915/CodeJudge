def solution(order):
    answer = 0
    container = []
    idx = 1
    cnt = 0
    while idx < len(order) + 1:
        container.append(idx)
        while container and container[-1] == order[cnt]:
            cnt += 1
            container.pop()
        idx += 1

    return cnt