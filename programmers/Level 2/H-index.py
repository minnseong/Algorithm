# Programmers 01/21 2022
# H-index

def solution(citations):
    answer = []
    
    citations.sort()
    rg = max(len(citations), max(citations))

    for i in range(rg):
        h = i
        moreCnt = 0
        for j in citations:
            if j >= i:
                moreCnt += 1
        if h <= moreCnt and h >= len(citations)-moreCnt:
            answer.append(h)

    return max(answer)

print(solution([0,0,0,1]))
