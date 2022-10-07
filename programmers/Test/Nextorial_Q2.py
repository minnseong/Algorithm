# 넥토리얼 코딩테스트 10/07 2022
# Q2 - 10/15 시간초과

def getMaximumRemovals(order, source, target):

    answer = 0
    source_list = list(source)
    target_list = list(target)

    source_index = set([i for i in range(len(source_list))])
    for idx in order:
        source_list[idx-1] = ""
        source_index.remove(idx-1)

        j = 0
        for i in source_index:
            if target_list[j] == source_list[i]:
                j += 1
            if j == len(target_list):
                answer += 1
                break

        if j != len(target_list):
            break

    return answer

print(getMaximumRemovals([1,4,2,3,5], "hkbdi", "kd"))
print(getMaximumRemovals([1,2,3,4], "abcd", "abcd"))