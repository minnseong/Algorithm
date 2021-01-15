# Programmers 01/15 2021
# 가장 큰 수

# sort 정리
# variable.sort() : 원형을 변형시키고 정렬 / 오름차순
# = sorted() : 원형을 변형시키지 않고 정렬한 후 반환 / 오름차순
# variable.sort(reverse=True) : 내림차순
# sorted(list, key =?) : 정렬을 목적으로 하는 함수 값을 ? 넣는다.
# = variable.sort(key =?)
import functools

def compare(a,b):
    num1 = a+b
    num2 = b+a
    if int(num1) > int(num2):
        return 1
    elif int(num1) < int(num2):
        return -1
    else:
        return 0

def solution(numbers):
    answer = ''

    # string으로 형변환
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(compare), reverse=True)

    if n[0]=='0':
        return '0'
    for num in n:
        answer += num

    return answer

print(solution([3, 30, 34, 5, 9]))