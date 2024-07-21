def cal_ans(n, idx):
    q, m = idx // n + 1, idx % n 
    
    if m == 0: m += n; q -= 1
    
    return max(q,m)


def solution(n, left, right):
    answer = []
    for idx in range(left, right+1):
        answer.append(cal_ans(n,idx + 1))
    return answer


if __name__ == "__main__":
    print(solution(4,7,14))