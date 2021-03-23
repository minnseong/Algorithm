# Programmers 03/23 2021
# 점프와 순간 이동

# 한번 -> K칸 앞으로 점프 -> K만큼 에너지 소모
#        (현재까지 온 거리) * 2 위치로 순간이동 -> 소모x
def solution(n):
    ans = 0

    while n != 0:
        if n & 1: # 짝 tel
            ans += 1
            n -= 1
        else: # 홀 jump
            n //= 2
    return ans

print(solution(5))

# 5 -> 1 j -> 2 p -> 4 p -> 1 j  energy 2
# 5 -> 1 jump : 4 -> 2 tel :  2 -> 1 tel : 1 -> 1 jump : 0  energy 2

# 6 -> 1 j -> 2 p -> 1 j -> 3 p  energy 2
# 6 -> 3 tel 3 -> 1 jump 2 -> 1 tel 1 -> 1 jump 0  energy 2