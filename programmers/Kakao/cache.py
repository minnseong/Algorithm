# Programmers 09/09 2022 다시 풀어보기 (코테 준비)
# KaKao 캐시

from collections import deque

def solution(cacheSize, cities):
    runTime = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for i in range(len(cities)):
        cities[i] = cities[i].upper()
        
    cache = deque([])
    cacheCount = 0
    for c in cities:
        if c in set(cache):
            cache.remove(c)
            cache.append(c)
            runTime += 1
                
        else:
            if cacheCount == cacheSize:
                cache.popleft()
                cache.append(c)
            else:
                cache.append(c)
                cacheCount += 1
            runTime += 5
    
    return runTime

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