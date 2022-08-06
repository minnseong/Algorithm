# 08/06 2022 
# 2022 토스 NEXT 개발자 챌린지 - Q1

def solution(s):
    answer = 0

    good_num = -1
    for i in range(len(s)-2):
        if s[i] == s[i+1] == s[i+2]:
            good_num = max(int(s[i]), good_num)
    
    if good_num == -1:
        return -1
    elif good_num == 0:
        return 0
    else:
        return good_num * 100 + good_num * 10 + good_num