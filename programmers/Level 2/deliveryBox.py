# Programmers 11/16 2022
# 택배상자

def solution(order):
    answer = 1
    
    container_belt = []
    assistant_container_belt = []
    
    # 첫번째 order
    for i in range(1, len(order)+1):
        if i < order[0]:
            assistant_container_belt.append(i)
        elif i > order[0]:
            container_belt.append(i)
    
    container_belt.reverse()
    
    for i in range(1, len(order)):
        if len(assistant_container_belt) >= 1 and order[i] < assistant_container_belt[-1]:
            break
        elif len(assistant_container_belt) >= 1 and order[i] == assistant_container_belt[-1]:
            assistant_container_belt.pop()
            answer += 1
        elif len(container_belt) >= 1 and order[i] == container_belt[-1]:
            container_belt.pop()
            answer += 1
        else:
            while len(container_belt) >= 1 and order[i] > container_belt[-1]:
                assistant_container_belt.append(container_belt.pop())
            answer += 1
            container_belt.pop()
    
    
    return answer