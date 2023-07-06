
def solution(scores):
    wanho_score = scores[0]
    sum_wanho_score = sum(scores[0])

    # 근무 태도 점수 내림차순, 동료 평가 점수 오름차순
    scores.sort(key=lambda x: (-x[0], x[1]))
    answer, limit = 1, 0

    for score in scores:
        sum_score = sum(score)
        if wanho_score[0] < score[0] and wanho_score[1] < score[1]:
            return -1
        
        # 성립하는 경우, incentive를 받는 직원
        if limit <= score[1]:
            if sum_wanho_score < sum_score:
                answer += 1
            limit = score[1]
    return answer
