# BackJoon 09/07 2021
# 22864 피로도

today = list(map(int, input().split()))
work = 0
fatigue = 0
days = 24

while days != 0:
    if fatigue + today[0] > today[3]:
        fatigue -= today[2]
        if fatigue < 0:
            fatigue = 0
    else:
        fatigue += today[0]
        work += today[1]

    days -= 1

print(work)
