# Programmers 02/28 2023
# 골드3 - 스티커 붙이기

def rotate_90(sticker):
    tmp_sticker = list()

    for i in range(len(sticker[0])):
        tmp = list()
        for j in range(len(sticker)-1, -1, -1):
            tmp.append(sticker[j][i])
        tmp_sticker.append(tmp)
    return tmp_sticker

def is_attachable(x, y, sticker):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == '0':
                continue
            if not (notebook[x+i][y+j] == True and sticker[i][j] == '1'):
                return False
    
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if (notebook[x+i][y+j] == True and sticker[i][j] == '1'):
                notebook[x+i][y+j] = False
    return True
                
import sys

N, M, K = map(int, sys.stdin.readline().split())

global notebook 
notebook = [[True] * M for _ in range(N)]
stickers = list()

for _ in range(K):
    h, w = map(int, sys.stdin.readline().split())
    sticker = list()
    for _ in range(h):
        sticker.append(sys.stdin.readline().split())
    stickers.append(sticker)

for sticker in stickers:
    for _ in range(4):
        flag = False
        for x in range(0, len(notebook)-len(sticker)+1):
            flag = False
            for y in range(0, len(notebook[0])-len(sticker[0])+1):
                if is_attachable(x, y, sticker):
                    flag = True
                    break
            if flag:
                break

        if flag:
            break
        else:
            sticker = rotate_90(sticker)

answer = 0
for i in range(len(notebook)):
    answer += notebook[i].count(False)

print(answer)