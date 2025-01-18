"""
    枚舉所有可能的 r ，我們需要關注其左側 l_i 的最大值 l_max
    對於每個右端點 r ，l 需要至少為 l_max + 1 才能滿足條件
"""

n, m = map(int, input().split())

intervals = []
for _ in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))

intervals.sort(key=lambda x: x[1])
ans = idx = 0
l_max = 0
for r in range(1, m + 1):
    while idx < n and intervals[idx][1] <= r:
        l_max = max(l_max, intervals[idx][0])
        idx += 1
    ans += r - (l_max + 1) + 1
print(ans)