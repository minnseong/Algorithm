# Programmers 04/03 2022
# 2018 KAKAO BLIND RECRUITMENT - 압축

def solution(msg):
    answer = []
    
    dic = dict()
    for i in range(1, 27):
        dic[chr(64+i)] = i
    idx = 27

    i, j = 0, 1
    while i < len(msg):
        while (msg[i:i+j] in dic):
            j += 1
            if i+j > len(msg):
                break
        j -= 1
        answer.append(dic[msg[i:i+j]])
        dic[msg[i:i+j+1]] = idx;
        idx += 1
        i += j
        j = 1

    return answer

print(solution("ABABABABABABABAB"))
