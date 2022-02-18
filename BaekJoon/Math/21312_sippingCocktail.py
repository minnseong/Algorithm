# BaekJoon 02/18 2022
# 21312 홀짝 칵테일

inputCocktail = list(map(int, input().split()))

oddCocktail = []
for i in inputCocktail:
    if i & 1:
        oddCocktail.append(i)

res = 1
if not oddCocktail:
    for i in inputCocktail:
        res *= i
else:
    for o in oddCocktail:
        res *= o

print(res)


