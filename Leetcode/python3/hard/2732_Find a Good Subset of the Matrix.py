#
# @lc app=leetcode id=2732 lang=python3
# @lcpr version=30204
#
# [2732] Find a Good Subset of the Matrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    結論挺好猜的，但證明看不懂思密達
    - 某一橫列的二進位表示為 0 、或某兩橫列的二進位表示 AND 運算後的結果為 0 就是答案
"""

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        pos = defaultdict(int)
        for i, row in enumerate(grid):
            mask = 0 # 計算當前橫列的二進位表示
            for j, x in enumerate(row):
                mask |= x << j
            if mask == 0: # 當前橫列的二進位表示為 0
                return [i]
            for k, p in pos.items(): # 是否有其他橫列與當前橫列的二進位表示 AND 運算後的結果為 0
                if mask & k == 0:
                    return [p, i]
            pos[mask] = i
        return []
# @lc code=end



#
# @lcpr case=start
# [[0,1,1,0],[0,0,0,1],[1,1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1],[1,1,1]]\n
# @lcpr case=end

#

