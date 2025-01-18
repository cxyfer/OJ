from heapq import *

n = int(input())
hp = list(map(int, input().split()))
heapify(hp)

ans = 0
while len(hp) > 1:
    x, y = heappop(hp), heappop(hp)
    ans += x + y
    heappush(hp, x + y)
print(ans)