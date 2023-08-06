def solution(cards):
    answer = []
    for i in range(len(cards)):
        tmp = []
        while cards[i] != -1:
            card = cards[i]
            tmp.append(card)
            cards[i] = -1
            i = card - 1
        answer.append(tmp)
    answer.sort(key=lambda x : len(x))
    return len(answer[-1]) * len(answer[-2])