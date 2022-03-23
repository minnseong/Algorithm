# Programmers 03/23 2022
# 단어 변환

def getAdjacency(word1, word2):
    cnt = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
        if cnt >= 2:
            return False
    return True

def solution(begin, target, words):

    stack = [[begin, 0]]
    visited = dict()

    for w in words:
        visited[w] = False
    
    while stack:
        word, cnt = stack.pop()

        if word == target:
            return cnt

        for w in words:
            if not visited[w] and getAdjacency(word, w):
                stack.append([w, cnt+1])
                visited[w] = True
    
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
