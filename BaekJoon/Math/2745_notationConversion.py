# BackJoon 09/08 2021
# 2745 진법 변환

# ord('A') = 65
num, notation = input().split()
res = 0

for i in range(len(num)-1, -1, -1):
    tmp = 0
    if num[i].isalpha():
        tmp = ord(num[i]) - 55
    else:
        tmp = int(num[i])
    res += (tmp*pow(int(notation), len(num)-1-i))

print(res)
