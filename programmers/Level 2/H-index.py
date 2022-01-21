# Programmers 01/21 2022
# H-index
# 시간복잡도 개선

def solution(citations):
    
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    
    return len(citations)

print(solution([3, 0, 6, 1, 5]))

'''
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
'''
