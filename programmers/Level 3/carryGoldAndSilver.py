# Programmers 07/11 2022
# 금과 은 운반하기

def solution(a, b, g, s, w, t):

    answer = (10**9) * (10**5) * 4
    start = 0
    end = 10**9 * 10**5 * 4

    while start <= end:
        mid = (start + end) // 2

        gSum, sSum, total = 0, 0, 0
        for i in range(len(t)):
            cnt = mid // (t[i] * 2)

            if mid % (t[i] * 2) >= t[i]:
                cnt += 1
            
            gSum += g[i] if w[i] * cnt > g[i] else w[i] * cnt
            sSum += s[i] if w[i] * cnt > s[i] else w[i] * cnt
            total += (g[i] + s[i]) if (g[i] + s[i] < cnt * w[i]) else cnt * w[i]

        if gSum >= a and sSum >= b and total >= a +b :
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    return answer

print(solution(10, 10, [100], [100], [7], [10]))