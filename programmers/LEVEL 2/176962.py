from collections import deque


# 시간 계산 함수
def cal_time(time):
    hour, minute = map(int, time.split(':'))
    total_time = hour * 60 + minute
    return total_time


def solution(plans):
    answer = []
    # 시간 순으로 정렬
    plans = [(name, cal_time(time), int(playtime)) for name, time, playtime in plans]
    plans.sort(key=lambda x: x[1])
    stack = deque()

    now_time = plans[0][1]

    for i in plans:
        second_name, second_time, second_playtime = i

        while stack:
            first_name, first_playtime = stack.pop()
            # 과제가 다음 과제 전에 끝나는 경우
            if now_time + first_playtime <= second_time:
                now_time = now_time + first_playtime
                answer.append(first_name)
            # 과제가 끝나기 전에 다음 과제가 오는 경우
            else:
                stack.append((first_name, (now_time + first_playtime) - second_time))
                break

        stack.append((second_name, second_playtime))
        now_time = second_time

    # 남은 과제들 순서대로 삽입
    while len(stack) != 0:
        answer.append(stack.pop()[0])

    return answer