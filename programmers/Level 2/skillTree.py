# Programmers 01/20 2022
# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    flag = True

    for st in skill_trees:
        sIdx = []
        for s in skill:
            tmpS = st.find(s) if st.find(s) >= 0 else 100
            sIdx.append(tmpS)
        
        if sIdx == sorted(sIdx):
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

# 2 4 100 : O -> 2 4 100 -> 같음
# 100 2 4 : X -> 2 4 100 -> 다름
# 2 100 4 : X  -> 2 4 100 -> 다름
