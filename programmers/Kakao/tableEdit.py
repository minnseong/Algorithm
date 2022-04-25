# Programmers 04/25 2022
# 표 편집

def solution(n, k, cmd):
    answer = ['O'] * n

    table = dict()
    deleteBuffer = []
    cur = k
    for i in range(n):
        table[i] = [i-1, i+1]
    

    for c in cmd:
        if c[0] == 'U':
            for _ in range(int(c.split(' ')[1])):
                cur = table[cur][0]
        elif c[0] == 'D':
            for _ in range(int(c.split(' ')[1])):
                cur = table[cur][1]
        elif c[0] == "C":
            if table[cur][0] == -1:
                table[table[cur][1]][0] = -1
                deleteBuffer.append(cur)
                answer[cur] = 'X'
                cur = table[cur][1]
            elif table[cur][1] == n:
                table[table[cur][0]][1] = n
                deleteBuffer.append(cur)
                answer[cur] = 'X'
                cur = table[cur][0]
            else:
                table[table[cur][0]][1] = table[cur][1]
                table[table[cur][1]][0] = table[cur][0]
                deleteBuffer.append(cur)
                answer[cur] = 'X'
                cur = table[cur][1]
        elif c[0] == 'Z':
            d = deleteBuffer.pop()
            if table[d][0] == -1:
                table[table[d][1]][0] = d
            elif table[d][1] == n:
                table[table[d][0]][1] = d
            else:
                table[table[d][1]][0] = d
                table[table[d][0]][1] = d
            answer[d] = 'O'
    return ''.join(answer)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))