#
# @lc app=leetcode id=861 lang=python3
# @lcpr version=30201
#
# [861] Score After Flipping Matrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Greedy
        為使和最大，首先要確保每個row的最高位都是1。
        再來遍歷每一個直行，如果該直行的1的數量小於0的數量，則翻轉該直行，使得該直行的貢獻最大。
    """
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m): #  確保每個row的最高位都是1
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        for j in range(1, n): # 從第二個col開始，使該col的貢獻最大
            cnt = sum(grid[i][j] for i in range(m))
            if cnt < m - cnt: # 翻轉的貢獻會比不翻轉大
                for i in range(m):
                    grid[i][j] ^= 1
        ans = 0 # 計算答案
        for i in range(m):
            for j in range(n):
                ans += grid[i][j] << (n - 1 - j)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[0,0,1,1],[1,0,1,0],[1,1,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0]]\n
# @lcpr case=end

#

