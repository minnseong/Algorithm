# BaekJoon 01/30 2022
# 20291 파일 정리

'''
    딕셔너리 정렬 -> sort 함수 사용 불가, output이 list 형태이다.
    dic = {'a':3, 'b':2, 'c':1}

    1. key 기준으로 정렬 (오름차순)
    dic = sorted(dic.items())
    output) [('a', 3), ('b', 2), ('c', 1)]

    2. key 기준으로 정렬 (내림차순)
    dic = sorted(dic.items(), key = lambda item: item[0], reverse= True)
    output) [('c', 1), ('b', 2), ('a', 3)]

    3. value 기준으로 정렬 (오름차순)
    dic = sorted(dic.items(), key = lambda item: item[1])
    output) [('c', 1), ('b', 2), ('a', 3)]

    4. value 기준으로 정렬 (내림차순)
    dic = sorted(dic.items(), key = lambda item: item[1], reverse=True)
    output) [('a', 3), ('b', 2), ('c', 1)]
'''

import sys

N = int(input())
file = dict()

for _ in range(N):
    name, extension = sys.stdin.readline().strip().split(".")
    if extension in file:
        file[extension] += 1
    else:
        file[extension] = 1

file = sorted(file.items())

for f in file:
    print(f[0], end=" ")
    print(f[1])