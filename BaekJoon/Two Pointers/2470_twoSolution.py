# BackJoon 12/28 2021
# 2470 두 용액

N = int(input())
water = list(map(int, input().split()))
water.sort()
ans = [water[0], water[-1], water[0]+water[-1]]
        
i = 0
j = N-1
while i != j:
    if abs(water[i]+water[j]) < abs(ans[2]):
        ans[0] = water[i]
        ans[1] = water[j]
        ans[2] = water[i] + water[j]
    
    if abs(water[i]+water[j-1]) >= abs(water[j]+water[i+1]):
        i += 1
    else:
        j -= 1

if ans[0] > ans[1]:
    print(str(ans[1]) + " " + str(ans[0]))
else:
    print(str(ans[0]) + " " + str(ans[1]))

# 시간 초과
# for i in range(N-1):
#     for j in range(i+1, N):
#         if abs(ans[2]) > abs(water[i] + water[j]):
#             ans[0] = water[i]
#             ans[1] = water[j]
#             ans[2] = water[i] + water[j]
#         if ans[2] == 0:
#             break

# if ans[0] > ans[1]:
#     print(str(ans[1]) + " " + str(ans[0]))
# else:
#     print(str(ans[0]) + " " + str(ans[1]))