# BaekJoon 10/09 2021
# 21314 민겸 수

MK = input()
M, N = [], []

tmp = ""
ttmp = ""
for i in range(len(MK)):
    if MK[i] == 'M':
        tmp += 'M'
        ttmp += 'M'
        if i == len(MK) - 1:
            M.append(tmp)
            N.append(ttmp)
    if MK[i] == 'K':
        if ttmp != '':
            N.append(ttmp)
            ttmp = ''
        tmp += MK[i]
        M.append(tmp)
        N.append('K')
        tmp = ""

maxNum = ""
minNum = ""
for k in M:
    if k[-1] == "K":
        maxNum += '5'
        maxNum += '0' * (len(k) - 1)
    else:
        maxNum += '1' * (len(k))

for k in N:
    if k == "K":
        minNum += '5'
    else:
        minNum += '1'
        minNum += '0' * (len(k) - 1)

print(maxNum)
print(minNum)
