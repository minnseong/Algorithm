# Programmers 02/01 2021
# K번째수

def solution(array, commands):
    answer = []
    commands_length = len(commands)

    for i in range(commands_length):
        tmp = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(tmp[commands[i][2]-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

'''
    for문 사용 - 2차원 배열
    
    위 code 다른 풀이.
    
    for i in commands:
        tmp = array[i[0]-1 : i[1]]
        tmp.sort()
        answer.append(tmp[i[2]-1])
    
    return answer
        
'''