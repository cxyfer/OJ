#
# @lc app=leetcode id=646 lang=python3
# @lcpr version=30204
#
# [646] Maximum Length of Pair Chain
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    Greedy
    Activit Selection Problem
"""
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        ans = 0
        last = float('-inf')
        for st, ed in pairs:
            if st > last:
                last = ed
                ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,2],[2,3],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[7,8],[4,5]]\n
# @lcpr case=end

#

