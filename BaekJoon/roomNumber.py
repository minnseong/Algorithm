# BaekJoon 01/25 2021
# 1475번 방번호

num_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
_input = input()

for i in _input:
    num_arr[int(i)] += 1
sixNine = int(num_arr[6]) + int(num_arr[9])

if sixNine % 2 == 0:
    sixNine = int(sixNine / 2)
else:
    sixNine = int(sixNine / 2) + 1

num_arr[6] = 0
num_arr[9] = 0

if sixNine >= max(num_arr):
    print(sixNine)
else:
    print(max(num_arr))

# 1234699