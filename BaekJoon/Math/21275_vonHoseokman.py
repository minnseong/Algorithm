# BaeJoon 09/23 2021
# 21275 폰 호석만
# - 67

def chNotation(num, n):
    res = 0
    num = num[::-1]
    for i in range(len(num)):
        if num[i].isdigit():
            res += int(num[i]) * pow(n, i)
        else:
            res += (ord(num[i])-87) * pow(n, i)
    return res


A, B = input().split()
A_num = []
B_num = []
cnt = 0
AB_num = 0

for i in range(2, 37):
    A_num.append(chNotation(A, i))

print(A_num)
for j in range(2, 37):
    if chNotation(B, j) in A_num:
        cnt += 1
        AB_num = chNotation(B, j)
        print(AB_num)

print(cnt)
if cnt == 0:
    print('Impossible')
elif cnt == 1:
    print(str(AB_num) + " " + str(A_num.index(AB_num)+1) +
          str(B_num.index(AB_num)+1))
else:
    print('Multiple')
