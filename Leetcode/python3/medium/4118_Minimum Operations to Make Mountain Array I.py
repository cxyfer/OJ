#
# @lc app=leetcode id=4118 lang=python3
#
# [4118] Minimum Operations to Make Mountain Array I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Biweekly Contest 196 - Q3
前後綴分解 + 前綴最小值優化DP

1. 值域上界分析：
   設山頂位置為 peak (0 < peak < n - 1)，則陣列中任意位置 k 到山頂的距離 |peak - k| <= n - 2。
   若將最終陣列每個元素壓低至 b[k] = min(a[k], max(nums) + (n - 2) - |peak - k|)：
   - 由於 (n - 2) - |peak - k| >= 0，所有被調降的元素仍滿足 b[k] >= max(nums) >= nums[k] >= 1，操作次數只會減少不會增加。
   - 兩側分別是兩個嚴格單調序列逐點取 min，因此依然維持嚴格遞增與嚴格遞減的山形性質。
   故最優解中所有元素的上界不超過 U = max(nums) + n - 2。

2. 前綴 DP 與前綴最小值優化：
   定義 f[i][j] 表示考慮前 i 個數，使其嚴格遞增（且皆 >= 1）並以 j 結尾的最小操作次數。
   由於嚴格遞增且最小值為 1，第 i 個數至少為 i，故 j 的範圍為 [i, U]。
   狀態轉移方程：
       f[i][j] = min(f[i - 1][k] for k in [i - 1, j - 1]) + |nums[i - 1] - j|
   隨著 j 遞增，轉移區間的右端點每次只增加 1，可用變數 pre_min 維護前綴最小值，將轉移降至 O(1)。
   將陣列反轉後做同樣的 DP 再反轉回來，即可得到後綴嚴格遞減的最小操作次數 suf。

3. 前後綴合併：
   枚舉山頂位置 i (1-indexed，範圍 [2, n - 1]，對應原陣列 nums[i - 1]) 與山頂的值 j：
   - 左側有 i 個數，故 j >= i；右側有 n - i + 1 個數，故 j >= n - i + 1，因此 j in [max(i, n - i + 1), U]。
   - pre[i][j] 與 suf[i - 1][j] 重複計算了山頂 nums[i - 1] 變成 j 的代價，需減去一次 |nums[i - 1] - j|。
   - 若 n < 3，無法構成山形陣列，回傳 -1。

時間複雜度：O(n * U)，其中 U = max(nums) + n - 2
空間複雜度：O(n * U)
"""
# @lc code=start
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        U = max(nums) + n - 2
        
        def do(nums: list[int]) -> int:
            # f[i][j] 表示考慮前 i 個數，使其遞增，且最後一個數是 j 的最小操作次數
            # f[i][j] = min(f[i-1][i-1...j-1]) + abs(nums[i] - j)
            f = [[inf] * (U + 1) for _ in range(n + 1)]
            f[0] = [0] * (U + 1)
            for i, x in enumerate(nums, 1):
                pre_min = inf
                for j in range(i, U + 1):
                    # f[i][j] = min(f[i - 1][k] for k in range(i - 1, j)) + abs(x - j)
                    pre_min = min(pre_min, f[i - 1][j - 1])
                    f[i][j] = pre_min + abs(x - j)
            return f


        pre = do(nums)
        suf = do(nums[::-1])[::-1]

        ans = inf
        for i in range(2, n):
            x = nums[i - 1]
            for j in range(max(i, n - i + 1), U + 1):
                ans = min(ans, pre[i][j] + suf[i - 1][j] - abs(x - j))
        return ans if ans < inf else -1
# @lc code=end

sol = Solution()
print(sol.minOperations([2,2,3]))  # Output: 2