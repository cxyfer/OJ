"""
P4147 玉蟾宫
https://www.luogu.com.cn/problem/P4147

本題和 85. Maximal Rectangle 完全相同，都是在求矩陣中最大的矩形面積。
枚舉以每一行為底邊，則可以構造出柱狀圖，將問題轉化為 84. Largest Rectangle in Histogram。

可以用三次遍歷，在維護左右邊界後計算答案，也能利用單調棧的性質在維護左邊界時計算答案。

強烈推薦閱讀靈神題解：
https://leetcode.cn/problems/largest-rectangle-in-histogram/solutions/2695467/dan-diao-zhan-fu-ti-dan-pythonjavacgojsr-89s7
"""


def solve():
    n, m = map(int, input().split())
    matrix = [input().split() for _ in range(n)]

    ans = 0
    heights = [0] * (m + 2)
    for row in matrix:
        for i, ch in enumerate(row, start=1):
            heights[i] = heights[i] + 1 if ch == "F" else 0
        # 84. Largest Rectangle in Histogram
        st = []
        for right, x in enumerate(heights):
            while st and x < heights[st[-1]]:
                idx = st.pop()  # idx 為當前的柱子
                if st:
                    # right 為右邊比當前矮的位置，left = st[-1] 為左邊比當前矮的位置
                    left = st[-1]
                    # 高度為 heights[idx] 的柱子可以向左右延伸的最大寬度為 right - left - 1
                    ans = max(ans, heights[idx] * (right - left - 1))
            st.append(right)
    print(ans * 3)


if __name__ == "__main__":
    solve()
