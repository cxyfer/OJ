#
# @lc app=leetcode id=3152 lang=python3
# @lcpr version=30202
#
# [3152] Special Array II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # s = list(accumulate([1 if x & 1 == y & 1 else 0 for x, y in pairwise(nums)], initial=0)) # prefix sum
        # return [True if s[r] - s[l] == 0 else False for l, r in queries]
        n = len(nums)
        special = [0] * n
        for i in range(1, n):
            if nums[i] & 1 == nums[i - 1] & 1:
                special[i] = 1
        s = list(accumulate(special)) # prefix sum
        ans = []
        for l, r in queries:
            ans.append(True if s[r] - s[l] == 0 else False)
        return ans
# @lc code=end



#
# @lcpr case=start
# [3,4,1,2,6]\n[[0,4]]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,1,6]\n[[0,2],[2,3]]\n
# @lcpr case=end

#

