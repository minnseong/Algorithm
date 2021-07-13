from collections import deque

testcase = int(input())

for _ in range(testcase):
    N, M = map(int, input().split())
    priority = deque(list(map(int, (input().split()))))
    queue = deque([i for i in range(N)])

    cnt = 1
    while True:
        maxPriority = max(priority)
        d, p = queue.popleft(), priority.popleft()

        if maxPriority != p:
            queue.append(d)
            priority.append(p)
        else:
            if d == M:
                print(cnt)
                break
            cnt += 1




