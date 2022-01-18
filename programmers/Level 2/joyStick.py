# Programmers 01/18 2022
# 조이 스틱
def checkAlla(s):
    if len(s) != 0 and s.count("A") == len(s):
        return True
    else:
        return False

def solution(name):
    answer = 0
    alpha = dict()

    for i in range(26):
        alpha[chr(65+i)] = i
    
    if len(name) > 1 and name[1] != "A":
        for i in range(len(name)):
            if alpha[name[i]] > 13:
                answer += (26-alpha[name[i]])
            else:
                answer += alpha[name[i]]
            
            if checkAlla(name[i+1:]):
                break
            
            if i < len(name)-1:
                answer += 1
    else:
        name = (name[0] + name[::-1])[:-1]
        for i in range(len(name)):
            if alpha[name[i]] > 13:
                answer += (26-alpha[name[i]])
            else:
                answer += alpha[name[i]]

            if checkAlla(name[i+1:]):
                break
            
            if i < len(name)-1:
                answer += 1

    return answer

print(solution("ABABAAAAAAABA"))
