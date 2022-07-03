# Programmers 07/03 2022
# 2022 Dev-Matching: 웹 백엔드 개발자(상반기)-2
# 93

def solution(grade):
    answer = 0

    i = 0
    while i < len(grade)-1:
        if grade[i] > grade[i+1]:
            answer += (grade[i]-grade[i+1])
            grade[i] = grade[i+1]
            i = -1
        i += 1
    
    return answer

print(solution([1,3,3,2,2,2,2,5]))