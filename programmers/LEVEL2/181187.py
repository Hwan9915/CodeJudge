from math import isqrt


def solution(r1, r2):
    r2_dots = 0
    # x 좌표로 계산
    for x in range(1, r2 + 1):
        y2 = isqrt(r2 ** 2 - x ** 2)

        # x와 평행한 선을 기준으로 r1과 r2가 모두 걸칠 때
        if x < r1:
            y1 = isqrt(r1 ** 2 - x ** 2)
            # 선 위에 점이 있는 경우
            if r1 ** 2 - x ** 2 == y1 ** 2:
                y1 = y1 - 1

        else:
            y1 = 0
            r2_dots += 1

        r2_dots = r2_dots + y2 - y1
    # 상하좌우 대칭이므로 4를 곱한다.
    return r2_dots * 4
