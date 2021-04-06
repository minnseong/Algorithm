# Programmers 04/03 2021
# KaKao 캐시
from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        return 5 * len(cities)

    for i in cities:
        i = i.lower()
        if i not in cache:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(i)
            answer += 5
        else:
            cache.remove(i)
            cache.append(i)
            answer += 1

    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))