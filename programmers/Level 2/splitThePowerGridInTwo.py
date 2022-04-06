# Programmers 04/06 2022
# 전력망을 둘로 나누기

from collections import defaultdict
import copy

def solution(n, wires):
    answer = 100

    dic = defaultdict(list)
    for w in wires:
        dic[w[0]].append(w[1])
        dic[w[1]].append(w[0])
    
    def dfs(startPoint, removePoint):
        cnt = 1
        stack = copy.deepcopy(dic[startPoint])
        stack.remove(removePoint)
        visited = [False] * (n+1)
        visited[startPoint] = True
        
        while stack:
            s = stack.pop()
            visited[s] = True
            cnt += 1

            for w in dic[s]:
                if not visited[w]:
                    stack.append(w)
        return cnt    
    
    for w in wires:
        answer = min(answer, abs(dfs(w[0], w[1]) - dfs(w[1], w[0])))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))