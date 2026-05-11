"""
ABC457G Catch All Apples
https://atcoder.jp/contests/abc457/tasks/abc457_g
Dilworth Theorem

設 ti < tj，則兩個位置可以由同一個機器人處理，等同於 |xi - xj| <= tj - ti
轉換成 ti + xi <= tj + xj 與 ti - xi <= tj - xj
那麼一個機器人能處理的點，會形成最長非嚴格遞增子序列。
則根據 Dilworth 定理，最少的機器人數量 = 最大反鏈長度
"""

from bisect import bisect_left


def solve():
    n = int(input())

    points = []
    for i in range(n):
        t, x = map(int, input().split())
        points.append((t + x, t - x))
    points.sort()

    # 求 v 的 LDS 長度
    f = []
    for _, v in points:
        idx = bisect_left(f, -v)
        if idx == len(f):
            f.append(-v)
        else:
            f[idx] = -v
    print(len(f))


if __name__ == "__main__":
    solve()
