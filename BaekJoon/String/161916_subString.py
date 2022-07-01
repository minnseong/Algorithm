# BaekJoon 07/01 2022
# 16916 부분 문자열

p = str(input())
s = str(input())

if len(s) > len(p):
    print(0)
else:
    i = 0
    ans = 0
    while i < len(p): 
        if p[i] == s[0]:
            cnt = 0
            for j in range(len(s)):
                if i < len(p) and p[i] == s[j]:
                    cnt += 1
                    i += 1
                else:
                    i -= 1
                    break
            if cnt == len(s):
                ans = 1
                break
        i += 1
    print(ans)

