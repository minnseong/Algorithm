# BaekJoon 08/20 2022
# 9466 텀 프로젝트

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    pick = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    team = set()

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []

            p = i
            while True:
                visited[p] = True
                cycle.append(p)

                p = pick[p]
                if visited[p]:
                    if p in cycle:
                        for c in cycle[cycle.index(p):]:
                            team.add(c)
                    break
    print(n - len(team))         





