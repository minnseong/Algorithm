# Programmers 01/21 2021
# 큰 수 만들기
# 테스트 케이스 10 시간초과. -> 해결.

def solution(number, k):
    answer = ""
    index = 0
    max_index = 0
    max_num = ""

    # 7자리 숫자중에 3개를 빼면 7개중에서 4개를 고르는 것.
    # 첫번째 자리를 두고
    # 3 2 3 4
    # 1 2 3 1 2 3 4 , k => 3개 : sel = 4

    for i in range(0, len(number)-k):
        max_num = number[index]
        max_index = index

        for j in range(index+1, i+k+1):
            if max_num < number[j]:
                max_num = number[j]
                max_index = j
            # 시간 단축 : 가장 큰수는 9이기 때문에, 반복문 중 가장 큰수가 9라면 break.
            if max_num == '9':
                break

        index = max_index + 1
        answer += max_num

    return answer

print(solution("1231234", 3))