# BaekJoon 01/27 2022
# 1244 스위치 켜고 끄기

def changeSwitch(idx):
    global switch

    if switch[idx-1] == 1:
        switch[idx-1] = 0
    else:
        switch[idx-1] = 1

switch_cnt = int(input())
switch = list(map(int, input().split()))
student_cnt = int(input())
student = [list(map(int, input().split())) for _ in range(student_cnt)]

for s in student:
    if s[0] == 1: # 남자
        index = s[1]
        while 1 <= index <= switch_cnt:
            changeSwitch(index)
            index += s[1]

    else: # 여자
        index = s[1]
        r, l = index-1, index+1
        flag = True
        while flag and r >= 1 and l <= switch_cnt:
            if switch[r-1] == switch[l-1]:
                r = r-1
                l = l+1
            else:
                flag = False

        if l-r == 2:
            changeSwitch(index)
        else:
            for i in range(r+1,l):
                changeSwitch(i)

for i in range(len(switch)//20+1):
    print(*switch[i*20:i*20+20])
        