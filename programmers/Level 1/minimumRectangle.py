# Programmers 01/16 2022
# 최소직사각형

def solution(sizes):

    w, h = 0 , 0
    
    for s in sizes:
        s.sort()

    for s in sizes:
        if s[0] > w:
            w = s[0]
        if s[1] > h:
            h = s[1]
    
    return w * h

print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))