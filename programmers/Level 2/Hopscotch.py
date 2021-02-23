# Programmers 02/23 2021
# 땅따먹기

def solution(land):
    answer = 0
    tmp = land.pop(0)
    # tmp = [1,2,3,5]
    # land = [5,6,7,8],[4,3,2,1]]

    for i in range(4):
        pick = [0, 1, 2, 3]
        pick.remove(i)
        # pick [1,2,3]
        for idx in range(len(land)):
            tmp[i] += max([land[idx][p] for p in pick])
            pick = [0, 1, 2, 3]
            pick.remove(land[idx].index(max([land[idx][p] for p in pick])))


    print(tmp)
    answer = max(i for i in tmp)
    return answer

print(solution([[1,2,3,5],[2,2,2,1],[8,1,1,1]]))