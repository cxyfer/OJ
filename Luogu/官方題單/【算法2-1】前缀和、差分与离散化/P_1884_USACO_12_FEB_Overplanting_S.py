"""
P1884 [USACO12FEB] Overplanting S
https://www.luogu.com.cn/problem/P1884
離散化 + 二維差分
"""


def solve():
    q = int(input())
    rects = []

    Xs = set()
    Ys = set()

    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        assert x1 <= x2 and y2 <= y1
        # 整理成左下/右上邊界
        rects.append((x1, y2, x2, y1))
        Xs.add(x1)
        Xs.add(x2)
        Ys.add(y2)
        Ys.add(y1)

    # 離散化
    Xs = sorted(Xs)
    Ys = sorted(Ys)
    mpX = {x: i for i, x in enumerate(Xs, start=1)}
    mpY = {y: i for i, y in enumerate(Ys, start=1)}

    n, m = len(Xs), len(Ys)

    # diff[i][j] 表示壓縮座標點上的差分
    diff = [[0] * (m + 1) for _ in range(n + 1)]

    # 二維差分更新
    for x1, y1, x2, y2 in rects:
        diff[mpX[x1]][mpY[y1]] += 1
        diff[mpX[x2]][mpY[y1]] -= 1
        diff[mpX[x1]][mpY[y2]] -= 1
        diff[mpX[x2]][mpY[y2]] += 1

    # 二維前綴和
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]

    # 計算面積
    ans = 0
    for i in range(1, n):
        dx = Xs[i] - Xs[i - 1]
        for j in range(1, m):
            dy = Ys[j] - Ys[j - 1]
            if diff[i][j] > 0:
                ans += dx * dy
    print(ans)


if __name__ == "__main__":
    solve()
