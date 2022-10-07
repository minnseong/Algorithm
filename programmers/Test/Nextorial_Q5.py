# 넥토리얼 코딩테스트 10/07 2022
# Q5 - 100

from collections import defaultdict
import heapq

def minCostPath(g_nodes, g_from, g_to, g_weight, x, y):
    nodes = len(set(g_from) | set(g_to))

    graph = defaultdict(list)

    for gf, gt, gw in zip(g_from, g_to, g_weight):
        graph[gf].append((gt, gw))
        graph[gt].append((gf, gw))

    def dijkstra(start):
        queue = []
        heapq.heappush(queue, (0, start))
        distance = [1e9] * (nodes + 1)
        distance[start] = 0

        while queue:
            dist, now = heapq.heappop(queue)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(queue, (cost, i[0]))
        return distance

    return dijkstra(1)[x] + dijkstra(x)[y] + dijkstra(y)[g_nodes]

print(minCostPath(5, [1,2,3,4,5,3], [2,3,4,5,1,5], [9,11,6,1,4,10], 2, 3))