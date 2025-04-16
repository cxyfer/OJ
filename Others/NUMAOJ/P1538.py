"""
【华为】20240410_1_云服务计费
https://niumacode.com/problem/P1538
"""

from collections import defaultdict

n = int(input())
records = []
for _ in range(n):
    ts, client, factor, ln = input().split(',')
    records.append((int(ts), client, factor, int(ln)))

m = int(input())
mp = defaultdict(int)
for _ in range(m):
    k, v = input().split(',')
    mp[k] = int(v)

ans = defaultdict(int)
vis = set()
for ts, client, factor, ln in records:
    if (ts, client, factor) in vis:
        continue
    vis.add((ts, client, factor))
    if 0 <= ln <= 100:
        ans[client] += mp[factor] * ln

for client, val in sorted(ans.items(), key=lambda x: x[0]):
    print(f"{client},{val}")