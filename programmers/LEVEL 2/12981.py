def solution(n, words):
    word_set = set()

    for idx, word in enumerate(words):
        if idx == 0:
            word_set.add(word)
            continue
        
        if word in word_set or words[idx-1][-1] != word[0]:
            return [idx%n+1,idx//n+1]
        word_set.add(word)

    else:
        return [0,0]