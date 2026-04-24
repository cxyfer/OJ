"""
P1719 最大加权矩形
https://www.luogu.com.cn/problem/P1719
二維前綴和 + Maximum Subarray Sum

最暴力的想法是枚舉矩形的左上角和右下角，然暴力後計算矩形內的和，
枚舉時需要 O(n^4) 的時間複雜度，計算時又需要 O(n^2) 的時間複雜度，總時間複雜度為 O(n^6)，顯然會超時。

我們可以先將矩形轉換為前綴和，然後枚舉矩形的左上角和右下角，
這樣計算矩形內的和的時間複雜度為 O(1)，總時間複雜度為 O(n^4)，以本題數據範圍來說是可以接受的。

但注意到如果固定上界和下界，我們可以將矩形轉換為一維陣列，
此時在該上下界的最大子矩形和就是該一維陣列的最大子陣列和。
這裡用對這個一維前綴和進行枚舉右維護左維護最小值，來求解最大子陣列和。
詳細解釋和其他方法可以見：https://gdst.dev/posts/LC-53/
"""


def solve1():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    s = [[0] * (n + 1) for _ in range(n + 1)]
    for i, row in enumerate(grid, start=1):
        for j, val in enumerate(row, start=1):
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + val

    ans = float("-inf")
    for x1 in range(1, n + 1):
        for y1 in range(1, n + 1):
            for x2 in range(x1, n + 1):
                for y2 in range(y1, n + 1):
                    ans = max(
                        ans,
                        s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1],
                    )
    print(ans)


def solve2():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    ss = [[0] * (n + 1) for _ in range(n + 1)]
    for i, row in enumerate(grid, start=1):
        for j, val in enumerate(row, start=1):
            ss[i][j] = ss[i - 1][j] + ss[i][j - 1] - ss[i - 1][j - 1] + val

    ans = float("-inf")
    for x1 in range(1, n + 1):
        for x2 in range(x1, n + 1):
            # 53. Maximum Subarray
            s = mn = 0
            for j in range(1, n + 1):
                s += ss[x2][j] - ss[x1 - 1][j] - ss[x2][j - 1] + ss[x1 - 1][j - 1]
                ans = max(ans, s - mn)
                mn = min(mn, s)
    print(ans)


# solve = solve1
solve = solve2

if __name__ == "__main__":
    solve()
