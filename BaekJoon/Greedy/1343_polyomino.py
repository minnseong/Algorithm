# BaekJoon 10/07 2021
# 1343 폴리오미노

board = input()
res = ""
bboard = ""

for i in range(len(board)-1):
    bboard += board[i]
    if board[i] != board[i+1]:
        bboard += ","
bboard += board[-1]
bb = bboard.split(",")

for b in bb:
    if 'X' in b and len(b) & 1:
        res = -1
        break
    elif '.' in b:
        res += b
    else:
        if len(b) % 4 == 0:
            res += ("AAAA" * (len(b)//4))
        elif len(b) == 2:
            res += "BB"
        else:
            res += ("AAAA" * (len(b)//4))
            res += "BB"

print(res)
