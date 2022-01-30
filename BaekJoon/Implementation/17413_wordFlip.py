# BaekJoon 01/30 2022
# 17413 단어 뒤집기 2

inputStr = input()
res = ''
tmp = ''

idx = 0
while idx < len(inputStr):
    s = inputStr[idx]
    
    if s == " ":
        res += (tmp[::-1] + " ")
        idx += 1
        tmp = ''

    elif idx == len(inputStr) -1 and tmp:
        tmp += s
        res += tmp[::-1]
        break

    elif s == "<":
        res += tmp[::-1]
        tmp = ''
        while inputStr[idx] != ">":
            tmp += inputStr[idx]
            idx += 1
        tmp += inputStr[idx]
        res += tmp
        tmp = ''
        idx += 1

    else:
        tmp += s
        idx += 1

print(res)
