# BaekJoon 03/11 2022
# 10798 세로읽기

strings = [input() for _ in range(5)]
lens = [len(strings[i]) for i in range(5)]

i = 0
while i < max(lens):
    if i < lens[0]:
        print(strings[0][i], end="") 
    if i < lens[1]:
        print(strings[1][i], end="") 
    if i < lens[2]:
        print(strings[2][i], end="") 
    if i < lens[3]:
        print(strings[3][i], end="") 
    if i < lens[4]:
        print(strings[4][i], end="")
    i +=1 

print()