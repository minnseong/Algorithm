# BaekJoon 10/30 2021
# 2630 색종이 만들기

N = int(input())
confetti = []
whiteCnt = 0
blueCnt = 0

for i in range(N):
    confetti.append(list(map(int, input().split())))


def countColor(arr):
    return [arr.count(0), arr.count(1)]


print(confetti[0].count(1))
