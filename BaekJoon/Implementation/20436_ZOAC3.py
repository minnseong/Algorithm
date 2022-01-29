# BaekJoon 01/29 2022
# 20436 ZOAC3

def getDistance(a, b):
    global loc
    return abs(loc[a][0] - loc[b][0])+abs(loc[a][1] - loc[b][1])

l, r = input().split()
inputAlpha = input()
time = len(inputAlpha)

alpha = ['zxcvbnm','asdfghjkl','qwertyuiop']

loc = dict()
leftKey = {'q','w','e','r','t','a','s','d','f','g','z','x','c','v'}

for i in range(len(alpha)):
    for j in range(len(alpha[i])):
        loc[alpha[i][j]] = [i, j]

for i in inputAlpha:
    if i in leftKey:
        time += getDistance(i, l)
        l = i
    else:
        time += getDistance(i, r)
        r = i

print(time)