# Programmers 01/29 2021
# 최솟값 만들기

def solution(A,B):
    answer = 0

    a = sorted(A)
    b = sorted(B, reverse = True)

    for i in range(0, len(A)):
        answer += a[i] * b[i]

    return answer

print(solution([1,4,2], [5,4,4]))

'''

# zip을 사용하여 풀이

    zip : 동일한 개수로 이루어진 자료형을 묶어 주는 역할
          여러 개의 리스트에서 값을 가져와서 처리가능

위 코드에 적용
    for a, b in zip(A, B):
        answer += a * b
        
'''