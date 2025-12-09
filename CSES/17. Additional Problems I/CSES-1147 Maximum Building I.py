"""
CSES-1147 Maximum Building I
https://cses.fi/problemset/task/1147
Same as 85. Maximal Rectangle

Monotonic Stack
將每一橫列視為一個以該橫列為底的柱狀圖，計算最大矩形面積即可。
"""
def solve():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    heights = [0] * (m + 2)
    ans = 0
    for row in grid:
        for i, ch in enumerate(row, 1):
            heights[i] = heights[i] + 1 if ch == '.' else 0

        # 做一次 CSES-1142 Advertisement 的計算
        st = []  # 單調遞增，保存的是下標
        for i, x in enumerate(heights):
            while st and heights[st[-1]] > x:
                # 以 A[st.pop()] 為最大高度的矩形，可以橫跨 [st[-1] + 1, i - 1]
                h = heights[st.pop()]
                w = i - st[-1] - 1
                ans = max(ans, h * w)
            st.append(i)
    print(ans)

if __name__ == "__main__":
    solve()