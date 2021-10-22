# BaekJoon 10/23 2021
# 6550 부분 문자열

while True:
    try:
        s, t = map(str, input().split())
    except:
        break
    cnt = 0
    start = 0

    for i in s:
        for j in range(start, len(t)):
            if i == t[j]:
                start = j + 1
                cnt += 1
                break

    if cnt == len(s):
        print('Yes')
    else:
        print('No')
