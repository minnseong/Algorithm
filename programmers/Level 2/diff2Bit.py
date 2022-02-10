# Programmers 02/10 2022
# 2개 이하로 다른 비트
# 시간 초과로 답 참고.

# bit 문제는 하드 코딩보다는 규칙이 있을 가능성이 높으니 문제를 풀기전에 규칙을 찾아보자.
def solution(numbers):
    answer = []

    for n in numbers:
        # 짝수일 경우 마지막 비트를 1을 올려주면 되므로, 원래 값에 + 1
        if not (n & 1):
            answer.append(n+1)
        else:
            n_bin = format(n, 'b')
            flag = n_bin.rfind('01')

            # 2진수 전환시 모든 비트가 1인 경우
            if flag == -1:
                answer.append(int('10'+n_bin[1:], 2))
            # 0이 섞여있는 경우
            else:
                answer.append(int(n_bin[:flag]+'10'+n_bin[flag+2:], 2))

    return answer

print(solution([2, 21]))

'''
시간 초과 코드 ..

def compare_bit(b1, b2):
    
    diff = abs(len(b1)-len(b2))

    if diff > 2:
        return 0

    for i in range(1, min(len(b1), len(b2))+1):
        if b1[-i] != b2[-i]:
            diff += 1
        if diff > 2:
            return 0
    
    return 1

def solution(numbers):
    answer = []

    for n in numbers:
        nBit = format(n, 'b')
        tmp = n
        while True:
            tmp += 1
            tmpBit = format(tmp, 'b')
            
            if compare_bit(nBit, tmpBit):
                answer.append(tmp)
                break
        
    return answer
'''