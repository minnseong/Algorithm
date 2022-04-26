# Programmers 04/26 2022
# 보석 쇼핑

def calculaterGap(x):
    return x[1]-x[0]

def solution(gems):
    answer = []
    gems_cnt = len(set(gems))
    gems_dict = dict()

    i, j = 0, 0
    gems_dict[gems[i]] = 1
    while i < len(gems) and j < len(gems):
        if len(gems_dict) < gems_cnt:
            j += 1
            if j >= len(gems):
                break
            gems_dict[gems[j]] = gems_dict.get(gems[j], 0) + 1
        else:
            answer.append([i+1, j+1])
            if gems_dict[gems[i]] == 1:
                del gems_dict[gems[i]]
            else:
                gems_dict[gems[i]] -= 1     
            i += 1
           
    answer.sort(key=lambda x: calculaterGap(x))
    return answer[0]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))