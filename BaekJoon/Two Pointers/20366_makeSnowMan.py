# BaekJoon 01/02 2022
# 20366 같이 눈사람 만들래?
import sys

N = int(input())
snow = list(map(int, input().split()))
snow.sort()
diff = 0

for i in range(0, N, 1):
    for j in range(N-1, -1, -1):
        r, l = i+1, j-1
        snowman1 = snow[i] + snow[j]

        while r < l:
            snowman2 = snow[r] + snow[l]

            if (r == 1 and l == N-2) or diff > abs(snowman1 - snowman2):
                diff = abs(snowman1 - snowman2)
                if diff == 0:
                    print(0)
                    sys.exit(0)

            if snowman1 > snowman2:
                r += 1
            else:
                l -= 1

print(diff)