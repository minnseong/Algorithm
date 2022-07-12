# Programmers 07/12 2022
# 단속 카메라

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])

    idx = 0
    while idx < len(routes):
        s, e = routes[idx]

        idxx = 0
        for i in range(idx, len(routes)):
            if routes[i][0] <= e <= routes[i][1]:
                idxx += 1
            else:
                break
        
        if idxx != 0:
            answer += 1
        idx += idxx

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
print(solution([[-100,100],[50,170],[150,200],[-50,-10],[10,20],[30,40]]))