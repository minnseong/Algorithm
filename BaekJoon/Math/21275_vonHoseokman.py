# BaekJoon 09/25 2021
# 21275 폰 호석만

def chNotation(num, n):
    res = 0
    num = num[::-1]
    for i in range(len(num)):
        if num[i].isdigit():
            res += int(num[i]) * pow(n, i)
        else:
            res += (ord(num[i])-87) * pow(n, i)
    return res


A, B = map(str, input().split())
A_num = []
B_num = []
cnt = 0
AB_num = 0
A_max = max([i for i in A])
B_max = max([i for i in B])

if A_max.isalpha():
    A_max = ord(A_max)-87
else:
    A_max = int(A_max)

if B_max.isalpha():
    B_max = ord(B_max)-87
else:
    B_max = int(B_max)

for i in range(A_max+1, 37):
    Anotation = chNotation(A, i)
    for j in range(B_max+1, 37):
        if i == j:
            continue
        else:
            if Anotation <= pow(2, 63) and Anotation == chNotation(B, j):
                res = [Anotation, i, j]
                cnt += 1

if cnt == 0:
    print('Impossible')
elif cnt == 1:
    print(str(res[0]) + " " + str(res[1]) + " " + str(res[2]))
else:
    print('Multiple')
