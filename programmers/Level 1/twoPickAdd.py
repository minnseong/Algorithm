# Programmers 01/29 2021
# 두 개 뽑아서 더하기

def solution(numbers):

    num = 0
    answer = []

    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            num = numbers[i] + numbers[j]
            if num not in answer:
                answer.append(num)

    return sorted(answer)

print(solution([5,0,2,7]))

'''

# itertools combinations (조합)
import itertools from combinations
 : combinations('ABCD', 2) --> AB AC AD BC BD CD
 : combinations(range(4), 3) --> 012 013 023 123
 
위 코드에 적용
    for a, b in list(combinations(numbers, 2)):
        if (a + b) not in answer:
            answer.append(a + b)
                
# itertools permutation (순열)
 : permutation('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
 : permutation(range(3)) --> 012 021 102 120 201 210

'''