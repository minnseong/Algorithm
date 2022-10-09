# SK텔레콤 코딩테스트 10/09 2022
# Q3

from collections import defaultdict

def solution(s, word_dict):
    answer = []

    word_index = defaultdict(list)

    for w in word_dict:
        word_index[w[0]].append(w)
    print(word_index)

    candidate = [[s[0], 0]]
    while candidate:
        word, word_count = candidate.pop()

        if word == s:
            answer.append(word_count)
            continue

        for w in word_index[word[-1]]:
            made_word = word + w[1:]
            if made_word == s[:len(made_word)]:
                candidate.append([made_word, word_count+1])

    return max(answer)

# print(solution("centerminus", ["cent", "center", "term", "terminus", "rm", "min", "minus", "us"]))

# cent + terminus
# cent + term + minus
# center + rm + minus

# 답 3