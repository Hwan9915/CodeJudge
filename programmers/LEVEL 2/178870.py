def solution(sequence, k):
    answer = [0, 1000001]
    sum_ = 0
    i = -1
    j = 0
    while True:
        if sum_ < k:
            i += 1
            if i >= len(sequence):
                break
            sum_ += sequence[i]

        else:
            sum_ -= sequence[j]
            if j >= len(sequence):
                break
            j += 1
        if sum_ == k:
            if abs(j - i) < abs(answer[1] - answer[0]):
                answer = [j, i]

    return answer
