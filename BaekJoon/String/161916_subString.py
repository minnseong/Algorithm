# BaekJoon 07/09 2022
# 16916 부분 문자열

def kmp_table(pattern):
    length = len(pattern)
    table = [0] * length
    j = 0

    for i in range(1, length):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
            
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    return table

def kmp(parent, pattern):
    table = kmp_table(pattern)
    parent_length = len(parent)
    pattern_length = len(pattern)

    j = 0
    for i in range(parent_length):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]

        if parent[i] == pattern[j]:
            if j == pattern_length - 1:
                return 1
            else:
                j += 1

    return 0

parent = input()
pattern = input()
print(kmp(parent, pattern))

''' 시간 초과
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
                    i -= (j)
                    break
            if cnt == len(s):
                ans = 1
                break
        i += 1
    print(ans)
'''