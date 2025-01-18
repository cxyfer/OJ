#
# @lc app=leetcode id=1673 lang=python3
# @lcpr version=30202
#
# [1673] Find the Most Competitive Subsequence
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        st = []
        for i, x in enumerate(nums):
            while st and st[-1] > x and len(st) + n - i > k:
                st.pop()
            if len(st) < k:
                st.append(x)
        return st
# @lc code=end



#
# @lcpr case=start
# [3,5,2,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,4,3,3,5,4,9,6]\n4\n
# @lcpr case=end

#

