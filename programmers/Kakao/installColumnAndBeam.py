# Programmers 05/07 2022
# 기둥과 보 설치

# 그때그때마다 체크가 필요함 -> 체크가 적절하지 않으면 바로 돌려놔야함.

def make_format(x,y,a):
    return str(x) + ',' + str(y) + ',' + str(a)

def check_frame(answer):
    for asw in answer:
        x, y, a = map(int, asw.split(','))
        if a == 0: # 기둥
            if y == 0 or make_format(x,y-1,0) in answer or make_format(x-1,y,1) in answer or make_format(x,y,1) in answer:
                continue
            return False
        elif a == 1: # 보
            if make_format(x,y-1,0) in answer or make_format(x+1,y-1,0) in answer or (make_format(x-1,y,1) in answer and make_format(x+1,y,1) in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    frame = set()
    
    for bf in build_frame:
        x, y, a, b = bf
        if b == 0: # 삭제
            frame.remove(make_format(x,y,a))
            if not check_frame(frame):
                frame.add(make_format(x,y,a))
        elif b == 1: # 생성
            frame.add(make_format(x,y,a))
            if not check_frame(frame):
                frame.remove(make_format(x,y,a))

    for fr in list(frame):
        x,y,a = map(int, fr.split(","))
        answer.append([x,y,a])
    
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
