# Programmers 03/21 2022
# 여행경로

def solution(tickets):

    tDict = dict()
    cnt = 1

    for t in tickets:
        cnt += 1
        if t[0] in tDict:
            tDict[t[0]].append(t[1])
        else:
            tDict[t[0]] = [t[1]]
        
    for val in tDict.values():
        val.sort(reverse=True)

    stack = ['ICN']
    log = []
    while stack:
        s = stack[-1]

        if s in tDict and len(tDict[s]) != 0:
            stack.append(tDict[s].pop())
            log.append(s)
        else:
            if len(stack) == cnt:
                break
            else:
                l = log.pop()
                tDict[l].insert(0, stack.pop())
                while len(tDict[l]) == 1:
                    l = log.pop()
                    tDict[l].insert(0, stack.pop())

    return stack

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))