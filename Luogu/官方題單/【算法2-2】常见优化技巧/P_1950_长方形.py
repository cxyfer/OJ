"""
P1950 长方形
https://www.luogu.com.cn/problem/P1950

枚舉底邊，則可以用類似 P4147 玉蟾宫 的思路，將問題轉化為求柱狀圖中以底邊為底的矩形數量
那麼對於每個區間 [l, r]，貢獻為 min(heights[l...r])，故所有為 sum(min(heights[l...r]) for r in range(m) for l in range(r+1))

1. 單調棧求左右邊界
區間的數量為 O(m^2) 的，直接枚舉區間顯然不能接受。
但高度的數量最多為 O(m)，故可以讓每個高度代表某些區間，並計算貢獻。

假設高度都是不同的，那麼我們可以用 h[i] 代表 min(heights[l...r]) == h[i] 的區間，
令 L[i] 為左邊第一個高度 < h[i] 的位置，R[i] 為右邊第一個高度 < h[i] 的位置，
則 h[i] 能代表的區間左端點可以為 [0, L[i]]，右端點可以為 [i, R[i]]，
區間數量為 (i - L[i] + 1) * (R[i] - i + 1)，貢獻為 h[i] * (i - L[i] + 1) * (R[i] - i + 1)

但高度可能相同，此時會發生重複計算的情況。
可以將 R[i] 改成為右邊第一個高度 <= h[i] 的位置，則對於包含多個 h[i] 的區間，一律交由最右側的 h[i] 代表。
這裡的說明暫略，手玩一下應該能理解。

此時只剩下如何快速求出 L[i] 和 R[i]，這可以利用單調棧解決。

類題：
- 3676. Count Bowl Subarrays
- 3878. Count Good Subarrays

2. 單調棧優化DP

令 f[i] = 以 i 為區間右端點的所有矩形數量，且 p 為左邊第一個高度 < h[i] 的位置。
則可以考慮左端點的情況：
1. 左端點位於 [0, p]：
   由於這些矩形的高度都至少為 h[p]，且 h[p + 1...i] 都至少為 h[i] > h[p]，
   故可以延伸到 i 的位置，貢獻為 f[p]
2. 左端點位於 [p+1, i]：
   由於 h[p + 1...i] 都至少為 h[i]，故貢獻為 h[i] * (i - p)
所求答案為 sum(f[i])
"""


def solve():
    n, m = map(int, input().split())
    matrix = [input().strip() for _ in range(n)]

    # 1. 單調棧求左右邊界
    def solve1(heights: list[int]) -> int:
        res = 0

        L = [0] * m
        R = [m - 1] * m

        st = []
        for i, x in enumerate(heights):
            while st and x <= heights[st[-1]]:
                st.pop()
            # 此時 st[-1] 為左邊第一個高度 < x 的位置，故左邊界為 st[-1] + 1
            L[i] = (st[-1] + 1) if st else 0
            st.append(i)

        st.clear()
        for i in range(m - 1, -1, -1):
            while st and heights[i] < heights[st[-1]]:
                st.pop()
            # 此時 st[-1] 為右邊第一個高度 <= x 的位置，故右邊界為 st[-1] - 1
            R[i] = (st[-1] - 1) if st else m - 1
            st.append(i)

        for i in range(m):
            res += (i - L[i] + 1) * (R[i] - i + 1) * heights[i]
        return res

    # 2. 單調棧優化DP
    def solve2(heights: list[int]) -> int:
        f = [0] * m  # f[j] = 以 j 為右端點的所有區間最小值總和
        st = []
        for i, h in enumerate(heights):
            while st and h <= heights[st[-1]]:
                st.pop()

            if st:
                # 此時 st[-1] 為左邊第一個高度 < h 的位置
                p = st[-1]
                # 左端點位於 [0, p]，且右端點為 p 的矩形都能繼續延伸到 i 的位置，此部分貢獻為 f[p]
                # 左端點位於 [p+1, i] 的矩形，其高度最大可以為 h，貢獻為 h * (i - p)
                f[i] = f[p] + heights[i] * (i - p)
            else:
                f[i] = heights[i] * (i + 1)

            st.append(i)

        return sum(f)

    ans = 0
    heights = [0] * m

    for row in matrix:
        for i, ch in enumerate(row):
            heights[i] = heights[i] + 1 if ch == "." else 0
        # ans += solve1(heights)
        ans += solve2(heights)
    print(ans)


if __name__ == "__main__":
    solve()
