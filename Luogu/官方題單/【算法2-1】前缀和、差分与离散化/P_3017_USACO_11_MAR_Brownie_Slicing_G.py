"""
P3017 [USACO11MAR] Brownie Slicing G
https://www.luogu.com.cn/problem/P3017
最大化最小值 -> 二分
"""


def solve():
    R, C, A, B = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]

    s = [[0] * (C + 1) for _ in range(R + 1)]
    for i, row in enumerate(grid, start=1):
        for j, val in enumerate(row, start=1):
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + val

    def area(x1, x2, y1, y2):
        return s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]

    tot = sum(sum(row) for row in grid)

    def check(mid):
        x1 = x2 = 1
        cntx = 0
        while x2 <= R:
            y1 = y2 = 1  # Two pointers
            cnty = 0
            while y1 <= C:
                # 二分需要 O(B log C) 次，而雙指標需要 O(C) 次，如果 B 遠比 C 小的話可以考慮二分
                # y2 = bisect_left(range(C + 1), mid, key=lambda y2: area(x1, x2, y1, y2))
                while y2 <= C and area(x1, x2, y1, y2) < mid:
                    y2 += 1
                if y2 > C:
                    break
                # assert area(x1, x2, y1, y2) >= mid
                cnty += 1
                if cnty == B:
                    break
                y1 = y2 = y2 + 1
            if cnty == B:
                cntx += 1
                if cntx == A:
                    return True
                x1 = x2 = x2 + 1
            else:
                x2 += 1
        return False

    left, right = 0, tot // (A * B)
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    print(right)


if __name__ == "__main__":
    solve()
