from heapq import *

n = int(input())
tasks = [list(map(int, input().split())) for _ in range(n)]
tasks.sort(key=lambda x: x[1])

ans = 0
tot = 0  # 要做的任務的總時間
hp = []  # Max Heap 所有要做的任務
for t1, t2 in tasks:
    if tot + t1 <= t2:  # 當前任務可以做
        tot += t1
        ans += 1
        heappush(hp, -t1)
    elif hp and -hp[0] > t1:  # 當前任務不能做，但前面做過了花費時間更長的任務，可以反悔改做這個
        mx = -heappop(hp)
        tot = tot - mx + t1  # 反悔
        heappush(hp, -t1)
print(ans)