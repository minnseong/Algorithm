# Programmers 02/10 2021
# Kakao 순위 검색
# 정확성 테스트 100%, 효율성 테스트 0%

def solution(info, query):
    answer = []

    for z in range(len(query)):
        answer.append(0)
    index = -1

    for q in query:
        query_list = q.split(" and ")
        tmp = query_list[len(query_list)-1]
        query_list.pop()
        query_list += (tmp.split(" "))
        index += 1

        # print('query: {}'.format(query_list))
        for s in info:
            info_list = s.split(' ')
            # if index == 5:
            # print('info: {}'.format(info_list))

            count = 0
            for m, n in zip(query_list, info_list):
                if m == '-':
                    count += 1
                elif m == n:
                    count += 1
                elif m.isdigit() and n.isdigit() and int(n) >= int(m):
                    count += 1
                else:
                    break

            if count == len(info_list):
                answer[index] += 1

    return answer


Q_info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"
]
Q_query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
]

print(solution(Q_info, Q_query))