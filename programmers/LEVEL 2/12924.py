def solution(n):
    answer = 0
    for i in range(1, n+1):
        tmp_ans = 0
        for j in range(i,n+1):
            tmp_ans += j
            if tmp_ans == n:
                answer += 1
            elif tmp_ans > n:
                break

    return answer

if __name__ == "__main__":
    print(solution(10))