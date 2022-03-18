# Programmers 03/18 2022
# 섬 연결하기

def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x: x[2])
    island = set([costs[0][0]])

    while len(island) != n:
        for c in costs:
            if c[0] in island and c[1] in island:
                pass
            elif c[0] in island or c[1] in island:
                island.add(c[0])
                island.add(c[1])
                answer += c[2]
                break
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[2,3,1],[2,3,8]]))