# Programmers 03/23 2021
# KaKao [3차]N진수 게임

def convert(n, base):
    t = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return t[r]
    else:
        return convert(q, base) + t[r]


def solution(n, t, m, p):
    answer = ''
    numStr = ""

# 1 2 3 4 5
    for i in range(t*m):
        numStr += convert(i, n)

    print(numStr)
    order = p - 1
    for i in range(t):
        answer += numStr[order]
        order += m

    return answer


# print(solution(2,4,2,1))
# print(solution(3,10,2,1))
print(solution(16, 16, 2, 2))

# 0 1 10 11 100 101 110 111 1000
# 0 1 1 1
# 13579bdf0123456789abcde1
# 2 1 : 1 3 5 7
# 2 2 : 2 4 6 8
# 4 2 : 2 6 10
