# 넥토리얼 코딩테스트 10/07 2022
# Q1 - 100

def minNum(samDaily, kellyDaily, difference):

    if kellyDaily < samDaily:
        return -1

    if samDaily == kellyDaily and difference >= 0:
        return -1


    answer = 0
    sam_solved = difference
    kelly_solved = 0

    while kelly_solved <= sam_solved:
        sam_solved += samDaily
        kelly_solved += kellyDaily
        answer += 1

    return answer

print(minNum(5, 5, 1))
print(minNum(4, 5, 1))