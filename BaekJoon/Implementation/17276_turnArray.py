# BaekJoon 02/01 2022
# 17276 배열 돌리기

'''
    얕은 복사 / 깊은 복사

    ex) a = [1,2,3]
    
    b=a # shallow copy 
    b=a[:] # 슬라이싱을 통한 할당 -> 서로 영향 x
    b=copy.copy(a) # shallowe copy
    b=copy.deepcopy(a) # deep copy

    ex) a = [[1,2,3], [1,2,3]]
    mutable 객체안에 mutable 객체가 있는 경우 -> list안에 list
    * mutable 객체 : list, set, dic // immutable : bool, int, float, tuple, str, frozenset
    b=a[:] 
    # a와 b의 주소값은 다르나 내부의 객체는 같은 주소값이기 때문에 
    a[0].append(1) 등 내부의 객체를 변경할 시 b의 내부객체도 동일하게 변경
    이 경우 b=copy.deepcopy(a) 를 사용해야만 deep copy가 가능하다.
'''

import sys
import copy

def turnClockwise(arr):
    newArr = copy.deepcopy(arr)
    for i in range(len(arr)):
        newArr[i][len(arr)//2] = arr[i][i]

    for i in range(len(arr)):
        newArr[i][len(arr)-1-i] = arr[i][(len(arr))//2]

    for i in range(len(arr)):
        newArr[len(arr)//2][i] = arr[len(arr)-i-1][i]
    
    for i in range(len(arr)):
        newArr[i][i] = arr[len(arr)//2][i]
    
    return newArr

T = int(input())

for _ in range(T):
    n, d = map(int, input().split())
    arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

    if d < 0:
        d = 360 + d
    d = d//45
    for _ in range(d):
        arr = turnClockwise(arr)

    for i in range(len(arr)):
        print(*arr[i])