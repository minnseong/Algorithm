# Programmers 09/05 2022 다시 풀어보기 (코테 준비)
# 2020 KAKAO BLIND RECRUITMENT - 문자열 압축

def splitString(s, i):
    array = []
    idx = 0
    while idx+i <= len(s):
        array.append(s[idx:idx+i])
        idx += i
    
    if s[idx:]:
        array.append(s[idx:])
    
    return array

def solution(s):
    result = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        arr = splitString(s, i)
        res = ""
        i, cnt = 0, 1 
        for j in range(1, len(arr)):
            if arr[i] == arr[j]:
                cnt += 1
            else:
                res += arr[i] if cnt == 1 else (str(cnt) + arr[i])
                i, cnt= j, 1

        res += arr[i] if cnt == 1 else (str(cnt) + arr[i])
        result = min(result, len(res))
        
    return result

# Programmers 09/09 2021
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
