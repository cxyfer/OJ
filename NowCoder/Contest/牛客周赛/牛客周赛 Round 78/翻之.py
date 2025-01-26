from collections import *

n, m = map(int, input().split())
grid = [input() for _ in range(n)]

cnt = defaultdict(int)
for col in zip(*grid):
    cnt[''.join(col)] += 1

print(max(cnt.values()))