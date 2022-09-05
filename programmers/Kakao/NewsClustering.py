# Programmers 09/06 2022 다시 풀어보기 (코테 준비)
# KaKao 뉴스 클러스터링

from collections import defaultdict

def breakByTwoLetters(s):
    s = s.upper()
    dic = defaultdict(int)
    for i in range(len(s)-1):
        if s[i].isalpha() and s[i+1].isalpha():
            dic[s[i:i+2]] += 1
    return dic
    
def getIntersection(dic1, dic2):
    dic = dict()
    for key in dic1.keys():
        if key in dic2.keys():
            dic[key] = min(dic1[key], dic2[key])
    
    for key in dic2.keys():
        if key in dic1.keys():
            dic[key] = min(dic1[key], dic2[key])

    return sum(dic.values())
    
def getUnion(dic1, dic2):
    dic = dict()
    for key in dic1.keys():
        if key in dic:
            dic[key] = max(dic[key], dic1[key])
        else:
            dic[key] = dic1[key]
            
    for key in dic2.keys():
        if key in dic:
            dic[key] = max(dic[key], dic2[key])
        else:
            dic[key] = dic2[key]

    return sum(dic.values())
    
def solution(str1, str2):
    dic1 = breakByTwoLetters(str1)
    dic2 = breakByTwoLetters(str2)
    
    try:
        result = getIntersection(dic1, dic2) / getUnion(dic1, dic2)
        return int(result * 65536)
    except:
        return 65536
    

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