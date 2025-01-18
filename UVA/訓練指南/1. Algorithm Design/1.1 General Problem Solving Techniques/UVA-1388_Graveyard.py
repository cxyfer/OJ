"""
1. 二分搜尋
    產生原本和新的座標，之後二分找最近的點
2. 座標變換
    將座標 * (n + m)，把新座標變換到 0, 1, 2, ... , n + m - 1
    此時原本座標為 i / n * (n + m)，四捨五入即可得到最近的新座標
"""

from bisect import *

while True:
    try:
        n, m = map(int, input().strip().split())
    except EOFError:
        break

    # A = [i * 1 / n for i in range(n)]
    # B = [j * 1 / (n + m) for j in range(n + m)]

    # ans = 0
    # for a in A:
    #     idx = bisect_left(B, a)
    #     if idx == 0:
    #         continue
    #     ans += min(abs(a - B[idx - 1]), abs(a - B[idx]))
    # ans *= 10000
    # print(f"{ans:.4f}")

    A = [i * (n + m) / n for i in range(n)]
    ans = 0
    for a in A:
        ans += abs(a - round(a))
    ans = ans * 10000 / (n + m)
    print(f"{ans:.4f}")