def solution(arr, brr):

    result = 0

    for i in range(len(arr)-1):
        if arr[i] > brr[i]:
            diff = arr[i] - brr[i]
            arr[i] = brr[i]
            arr[i+1] += diff
            result += 1

        elif arr[i] < brr[i]:
            diff = brr[i] - arr[i]
            arr[i] = brr[i]
            arr[i+1] -= diff
            result += 1

    return result

print(solution([3, 7, 2, 4], [4, 5, 5, 2]))
print(solution([6, 2, 2, 6], [4, 4, 4, 4]))