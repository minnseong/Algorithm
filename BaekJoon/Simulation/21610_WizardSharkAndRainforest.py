# BaekJoon 05/29 2022
# 1717 마법사 상어와 비바라기

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
flag = [[False] * n for _ in range(n)]

op = [list(map(int, input().split())) for _ in range(m)]

def move(cloud, d, s):
    if d == 1:
        for i in range(len(cloud)):
            cloud[i] = [cloud[i][0], (n+cloud[i][1]-s)%n]
            board[cloud[i][0]][cloud[i][1]] +=1
            flag[cloud[i][0]][cloud[i][1]] = True
    elif d == 2:
        for i in range(len(cloud)):
            cloud[i] = [(n+cloud[i][0]-s)%n, (n+cloud[i][1]-s)%n]
            board[cloud[i][0]][cloud[i][1]] +=1
            flag[cloud[i][0]][cloud[i][1]] = True
    elif d == 3:
        for i in range(len(cloud)):
            cloud[i] = [(n+cloud[i][0]-s)%n, cloud[i][1]]
            board[cloud[i][0]][cloud[i][1]] +=1
            flag[cloud[i][0]][cloud[i][1]] = True    
    elif d == 4:
        for i in range(len(cloud)):
            cloud[i] = [(n+cloud[i][0]-s)%n, (cloud[i][1]+s)%n]
            board[cloud[i][0]][cloud[i][1]] +=1
            flag[cloud[i][0]][cloud[i][1]] = True
    elif d == 5:
        for i in range(len(cloud)):
            cloud[i] = [cloud[i][0], (cloud[i][1]+s)%n]        
            board[cloud[i][0]][cloud[i][1]] +=1
            flag[cloud[i][0]][cloud[i][1]] = True
    elif d == 6:
        for i in range(len(cloud)):
            cloud[i] = [(cloud[i][0]+s)%n, (cloud[i][1]+s)%n]
            board[cloud[i][0]][cloud[i][1]] +=1
            flag[cloud[i][0]][cloud[i][1]] = True
    elif d == 7:
        for i in range(len(cloud)):
            cloud[i] = [(cloud[i][0]+s)%n, cloud[i][1]]
            board[cloud[i][0]][cloud[i][1]] +=1
            flag[cloud[i][0]][cloud[i][1]] = True
    elif d == 8:
        for i in range(len(cloud)):
            cloud[i] = [(cloud[i][0]+s)%n, (n+cloud[i][1]-s)%n]
            board[cloud[i][0]][cloud[i][1]] +=1
            flag[cloud[i][0]][cloud[i][1]] = True

def countDiagonal(loc):
    dir = [[-1,-1],[1,1],[-1,1],[1,-1]]
    cnt = 0
    for d in dir:
        dx, dy = loc[0] + d[0], loc[1] + d[1]
        if 0 <= dx < n and 0 <= dy < n and board[dx][dy] > 0:
            cnt += 1
    return cnt

def createCloud(flag):
    cloud = []
    for i in range(n):
        for j in range(n):
            if flag[i][j]:
                flag[i][j] = False
            elif board[i][j] >= 2:
                cloud.append((i,j))
                board[i][j] -= 2
    return cloud

cloud = []
for i in [[n-1,0], [n-1,1], [n-2,0], [n-2,1]]:
    cloud.append((i[0], i[1]))

for o in op:
    move(cloud, o[0], o[1])
    for c in cloud:
        board[c[0]][c[1]] += countDiagonal(c)
    cloud = createCloud(flag)

res = 0
for i in range(n):
    res += sum(board[i])

print(res)