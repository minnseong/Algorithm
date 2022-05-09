# Programmers 05/09 2022
# 2022 카카오 인턴 코딩 테스트 Q1
# 성공

def solution(survey, choices):
    answer = ''

    type_dict = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    type_arr = ['RT', 'CF', 'JM', 'AN']
    for s, c in zip(survey, choices):
        if c <= 3:
            type_dict[s[0]] += (4-c)
        elif c == 4:
            pass
        elif c >= 5:
            type_dict[s[1]] += (c-4)

    for t in type_arr:
        if type_dict[t[0]] >= type_dict[t[1]]:
            answer += t[0]
        else:
            answer += t[1]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
