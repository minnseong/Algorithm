# Programmers 01/12 2022
# KaKao 거리두기 확인하기

def getManhanttan(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def checkPX(place):
    P = [[False] * 5 for _ in range(5)]
    X = [[False] * 5 for _ in range(5)]

    Parr, Xarr = [], []
    for i in range(len(place)):
        for j in range(len(place[0])):
            if place[i][j] == 'P':
                P[i][j] = True
                Parr.append([i,j])
            elif place[i][j] == 'X':
                X[i][j] = True
                Xarr.append([i,j])

    return [P, Parr, X, Xarr]

def getManhanttan2(p):
    dir = [[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1],[-2,0],[0,-2],[2,0],[0,2]]
    res = []
    for d in dir:
        dx, dy = p[0]+d[0], p[1]+d[1]
        if 0 <= p[0]+d[0] < 5 and 0 <= p[1]+d[1] < 5:
            res.append([dx, dy])
    
    return res


def solution(places):
    answer = []

    for p in places:
        P, Parr, X, Xarr = checkPX(p)
        flag = True

        for point in Parr:
            m2 = getManhanttan2(point)

            for m in m2:
                x, y = m[0], m[1]
                if P[x][y]:
                    if getManhanttan([x,y], point) == 1:
                        flag = False
                        break
                    elif abs(point[0]-x) == 1 and abs(point[1]-y) == 1:
                        if not (X[point[0]][y] and X[x][point[1]]):
                            flag = False
                            break
                    else:
                        if not X[(point[0]+x) //2 ][(point[1]+y) //2]:
                            flag = False
                            break

            if not flag:
                answer.append(0)
                break
            
        if flag:
            answer.append(1)    
        
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))