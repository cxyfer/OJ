#
# @lc app=leetcode id=3159 lang=python3
# @lcpr version=30203
#
# [3159] Find Occurrences of an Element in an Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        # pos = [i for i, v in enumerate(nums) if v == x]
        # return [pos[q-1] if q <= len(pos) else -1 for q in queries]
        pos = []
        for i, v in enumerate(nums):
            if v == x:
                pos.append(i)
        ans = []
        for q in queries:
            ans.append(pos[q-1] if q <= len(pos) else -1)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,3,1,7]\n[1,3,2,4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n[10]\n5\n
# @lcpr case=end

#

