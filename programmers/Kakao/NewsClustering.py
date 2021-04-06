# Programmers 04/03 2021
# KaKao 뉴스 클러스터링

def solution(str1, str2):

    union = 0
    intersection = 0

    str1 = str1.lower()
    str2 = str2.lower()

    str1_dic = {}
    str2_dic = {}

    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if tmp.isalpha():
            if tmp in str1_dic:
                str1_dic[tmp] += 1
            else:
                str1_dic[tmp] = 1

    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        if tmp.isalpha():
            if tmp in str2_dic:
                str2_dic[tmp] += 1
            else:
                str2_dic[tmp] = 1

    print(str1_dic)
    print(str2_dic)

    for i in str1_dic:
        if i in str2_dic:
            intersection += min(str1_dic[i], str2_dic[i])

    for i in str1_dic:
        if i in str2_dic:
            union += max(str1_dic[i], str2_dic[i])
            str2_dic[i] = 0
        else:
            union += str1_dic[i]

    for i in str2_dic:
        union += str2_dic[i]

    if intersection == 0 and union == 0:
        answer = 1
    elif intersection == 0 or union == 0:
        answer = 0
    else:
        answer = intersection / union

    return int(answer * 65536)


print(solution("FRANCE", "french"))
print(solution("aaaa", "aa"))