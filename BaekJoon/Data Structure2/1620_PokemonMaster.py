import sys

N, M = map(int, sys.stdin.readline().strip().split())
pokemon = []
dic = {}

for i in range(N):
    tmp = sys.stdin.readline().strip()
    pokemon.append(tmp)
    dic[tmp] = i+1


for i in range(M):
    temp = sys.stdin.readline().strip()
    if temp.isdigit():
        print(pokemon[int(temp)-1])
    else:
        print(dic[temp])