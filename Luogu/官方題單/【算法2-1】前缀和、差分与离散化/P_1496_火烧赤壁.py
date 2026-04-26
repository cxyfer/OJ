"""
P1496 火烧赤壁
https://www.luogu.com.cn/problem/P1496
離散化 + 差分
"""

from itertools import pairwise


def solve():
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    # 離散化
    Xs = set()
    for l, r in queries:  # [l, r)
        Xs.add(l)
        Xs.add(r)
    Xs = sorted(Xs)
    mp = {x: i for i, x in enumerate(Xs)}
    m = len(Xs)

    # 差分
    diff = [0] * (m + 1)
    for l, r in queries:
        diff[mp[l]] += 1
        diff[mp[r]] -= 1

    ans = s = 0
    for i, (a, b) in enumerate(pairwise(Xs)):
        s += diff[i]
        if s > 0:
            ans += b - a

    print(ans)


if __name__ == "__main__":
    solve()
