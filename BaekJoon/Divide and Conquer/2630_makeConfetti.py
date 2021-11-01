# BaekJoon 11/01 2021
# 2630 색종이 만들기

N = int(input())
confetti = []
whiteCnt = 0
blueCnt = 0

for i in range(N):
    confetti.append(list(map(int, input().split())))


def checkConfetti(x, y, size):
    wCnt, bCnt = 0, 0
    global whiteCnt, blueCnt
    for i in range(x, x+size):
        for j in range(y, y+size):
            if confetti[i][j] == 0:
                wCnt += 1
            elif confetti[i][j] == 1:
                bCnt += 1
            else:
                return False

            if bCnt > 0 and wCnt > 0:
                return False

    if bCnt == 0 and wCnt > 0:
        whiteCnt += 1
        return True
    elif bCnt > 0 and wCnt == 0:
        blueCnt += 1
        return True


def changeConfetti(x, y, size):
    global confetti

    for i in range(x, x+size):
        for j in range(y, y+size):
            confetti[i][j] = -1


s = N
while s >= 1:
    for i in range(0, N, s):
        for j in range(0, N, s):
            if checkConfetti(i, j, s):
                changeConfetti(i, j, s)
    s //= 2

print(whiteCnt)
print(blueCnt)
