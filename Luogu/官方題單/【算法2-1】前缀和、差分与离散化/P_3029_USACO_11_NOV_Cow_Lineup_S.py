"""
P3029 [USACO11NOV] Cow Lineup S
https://www.luogu.com.cn/problem/P3029
離散化 + 滑動窗口
"""

from collections import defaultdict


def solve():
    n = int(input())
    cows = [tuple(map(int, input().split())) for _ in range(n)]

    k = len(set(col for _, col in cows))

    mapX = defaultdict(list)
    for x, col in cows:
        mapX[x].append(col)
    Xs = sorted(mapX.keys())

    ans = float("inf")
    cnt = defaultdict(int)
    left = 0
    for _, x in enumerate(Xs):
        for col in mapX[x]:
            cnt[col] += 1
        while len(cnt) == k:
            ans = min(ans, x - Xs[left])
            for col in mapX[Xs[left]]:
                cnt[col] -= 1
                if cnt[col] == 0:
                    del cnt[col]
            left += 1

    print(ans)


if __name__ == "__main__":
    solve()
