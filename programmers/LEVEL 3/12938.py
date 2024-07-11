def solution(n, s):
    answer = []
    
    if s<n:
        return [-1]
    
    max_num = s//n
    rest = s%n
    
    answer = [max_num for _ in range(n)]
    
    if rest != 0:
        for a in range(len(answer)):
            answer[a] += 1
            rest -= 1
            if rest == 0:
                break
    
    answer.sort()
    return answer

if __name__ == "__main__":
    print(solution(3,11))