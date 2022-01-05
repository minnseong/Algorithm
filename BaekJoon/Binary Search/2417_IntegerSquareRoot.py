# BaekJoon 01/05 2022
# 2417 정수 제곱근
import math

n = int(input())

start = 0
end = math.ceil(math.sqrt(2**63))+1
mid = 0

while True:
    mid = (start + end) // 2
    if mid > math.sqrt(n):
        end = mid
    else:
        start = mid
        
    if mid == math.ceil(math.sqrt(n)):
        print(mid)
        break