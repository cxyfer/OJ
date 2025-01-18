import sys
from functools import cache

buf = sys.stdin.read().split()
cin = lambda: buf.pop(0)

def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

while True:
    try:
        # n = int(input())
        n = int(cin())
    except IndexError:
        break
    points = [tuple(int(cin()) for _ in range(2)) for _ in range(n)] 

    @cache
    def dfs(i, j):
        assert i > j or (i == 0 and j == 0)
        if i == n - 1:
            return dist(points[i], points[j])
        res = dfs(i + 1, j) + dist(points[i], points[i + 1])
        if j != i + 1:
            res = min(res, dfs(i + 1, i) + dist(points[j], points[i + 1]))
        return res
    print(f"{dfs(0, 0):.2f}")