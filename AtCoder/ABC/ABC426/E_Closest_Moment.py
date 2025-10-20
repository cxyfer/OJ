"""
三分搜尋 (Ternary Search)

令 f(t) 表示時間 t 時，兩個點的最短距離的平方。
由於在兩點移動、或固定一點，另一點移動的情況下，
f(t) 是凹函數，因此可以三分搜尋找到最小的 f(t)。
"""

import math


def solve():
    ax1, ay1, ax2, ay2 = map(int, input().split())
    bx1, by1, bx2, by2 = map(int, input().split())

    p = math.sqrt((ax2 - ax1) ** 2 + (ay2 - ay1) ** 2)
    q = math.sqrt((bx2 - bx1) ** 2 + (by2 - by1) ** 2)

    def get_pos_a(t):
        if t >= p:
            return ax2, ay2
        return ax1 + (ax2 - ax1) * t / p, ay1 + (ay2 - ay1) * t / p

    def get_pos_b(t):
        if t >= q:
            return bx2, by2
        return bx1 + (bx2 - bx1) * t / q, by1 + (by2 - by1) * t / q

    def f(t):
        ax, ay = get_pos_a(t)
        bx, by = get_pos_b(t)
        return (ax - bx) ** 2 + (ay - by) ** 2

    def search(left, right):
        for _ in range(100):
            m1 = (left * 2 + right) / 3
            m2 = (left + right * 2) / 3
            if f(m1) < f(m2):
                right = m2
            else:
                left = m1
        return f(left)

    min_dist_sq = min(search(0.0, float(min(p, q))),
                      search(float(min(p, q)), float(max(p, q))))
    ans = math.sqrt(min_dist_sq)
    print(f"{ans:.12f}")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()