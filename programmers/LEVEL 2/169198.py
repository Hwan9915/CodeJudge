import math


# 좌표 계산
def cal_distance(x1, y1, x2, y2):
    result = math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)
    return result


def solution(m, n, startX, startY, balls):
    answer = []
    for endX, endY in balls:
        dots = []
        # 상
        if not (startX == endX and startY < endY):
            dots.append(cal_distance(startX, 2 * n - startY, endX, endY))
        # 하
        if not (startX == endX and startY > endY):
            dots.append(cal_distance(startX, -startY, endX, endY))
        # 좌
        if not (startX > endX and startY == endY):
            dots.append(cal_distance(-startX, startY, endX, endY))
        # 우
        if not (startX < endX and startY == endY):
            dots.append(cal_distance(2 * m - startX, startY, endX, endY))

        answer.append(round(min(dots), 2))

    return answer
