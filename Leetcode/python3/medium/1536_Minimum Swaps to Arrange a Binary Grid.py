#
# @lc app=leetcode id=1536 lang=python3
#
# [1536] Minimum Swaps to Arrange a Binary Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 預處理每一行的尾零個數，預設為 n，表示所有格子都是 0
        tail0 = [n] * n
        for i, row in enumerate(grid):
            for j in range(n - 1, -1, -1):
                if row[j] == 1:
                    tail0[i] = n - j - 1
                    break
        # Bubble Sort
        ans = 0
        for i in range(n):
            tgt = n - i - 1
            for j in range(i, n):
                if tail0[j] >= tgt:
                    # 把 j 往前移到 i 的位置，需要把 i 到 j-1 的元素往後移一位
                    ans += j - i
                    tail0.pop(j)
                    tail0.insert(i, tgt)
                    break
            else:
                # 沒有找到符合條件的元素
                return -1
        return ans
# @lc code=end

sol = Solution()
print(sol.minSwaps([[0,0,1],[1,1,0],[1,0,0]]))   #