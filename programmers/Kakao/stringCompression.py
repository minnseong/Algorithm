# Programmers 08/27 2021
# 2020 KAKAO BLIND RECRUITMENT - 문자열 압축

def split(str, n):
    arr = []

    for i in range(0, len(str), n):
        arr.append(str[i:i+n])

    return arr


def solution(s):
    count = []

    for i in range(1, len(s)+1):
        tmpArr = split(s, i)
        cnt = 1
        compression = ""

        for j in range(1, len(tmpArr)):
            prev, cursor = tmpArr[j-1], tmpArr[j]
            if prev == cursor:
                cnt += 1
            else:
                compression += (str(cnt) +
                                prev) if cnt > 1 else prev
                cnt = 1

        compression += (str(cnt) + tmpArr[-1]) if cnt > 1 else tmpArr[-1]
        count.append(len(compression))

    return min(count)


print(solution("aabbaccc"))
