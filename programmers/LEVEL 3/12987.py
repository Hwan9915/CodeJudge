def solution(A, B):
     answer, j = 0, 0
     A.sort(); B.sort()
    
     for i in range(len(B)):
        if A[j] < B[i]:
            answer += 1
            j += 1
            
     return answer