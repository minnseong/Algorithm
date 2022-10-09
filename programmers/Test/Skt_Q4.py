# SK텔레콤 코딩테스트 10/09 2022
# Q4

import copy

def do_shuffle(init, shuffles):

    result = [0] * len(init)

    for i in range(len(shuffles)):
        result[shuffles[i]-1] = init[i]

    return result


def solution(cards, shuffles):
    answer = []

    shuffle_dict = dict()
    for i in range(len(shuffles)):
        shuffle_dict[shuffles[i]-1] = i

    result = do_shuffle(cards, shuffles)
    print(result)
    candidate = []
    for i in range(len(result)):
        if cards[i] != result[i]:
            candidate.append([copy.deepcopy(cards), copy.deepcopy(result), i, 0])
    
    for i in range(len(candidate)):
        candidate[i].append(len(candidate))

    while candidate:
        card, result, idx, cnt, wrong_cnt = candidate.pop()
        # 1 1 2 2 2 1,  1 1 2 2 2 1 , 2 , 0 , 2
        result[idx] = card[idx]
        card[shuffle_dict[idx]] = card[idx]
        c = 0
        w_idx = []
        for i in range(len(result)):
            if card[i] != result[i]:
                c += 1
                w_idx.append(i)

        if c == 0:
            answer.append(cnt+1)
            continue

        if c < wrong_cnt:
            for i in range(len(w_idx)):
                candidate.append([card, result, w_idx[i], cnt+1, c])

    return min(answer)

# print(solution([1,1,2,2,1,1], [2,1,4,5,3,6])) # 1
# print(solution([1,2,3,4], [4,1,2,3])) # 3
print(solution([1,2,3,4,5], [5,4,2,3,1])) # 3
