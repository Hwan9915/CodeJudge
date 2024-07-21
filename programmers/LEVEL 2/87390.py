def cal_ans(n, idx):
    q, m = idx // n + 1, idx % n 
    
    if m == 0: m += n; q -= 1
    
    return max(q,m)


def solution(n, left, right):
    answer = []
    for idx in range(left, right+1):
        answer.append(cal_ans(n,idx + 1))
    return answer


def solution1(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer


if __name__ == "__main__":
    print(solution1(4,0,14))