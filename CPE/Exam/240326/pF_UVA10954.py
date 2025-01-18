"""
    Greedy + Heap
    tags: CPE-130528
"""
from heapq import *
import sys
buf = sys.stdin.read().split()
cin = lambda: buf.pop(0)

while True:
    # n = int(input())
    n = int(cin())
    if n == 0:
        break
    # hp = list(map(int, input().split()))
    hp = [int(cin()) for _ in range(n)]
    heapify(hp)
    ans = 0
    while len(hp) > 1:
        a = heappop(hp)
        b = heappop(hp)
        cost = a + b
        ans += cost
        heappush(hp, cost)
    print(ans)