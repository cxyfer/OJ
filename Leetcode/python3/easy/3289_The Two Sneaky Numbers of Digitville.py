#
# @lc app=leetcode id=3289 lang=python3
# @lcpr version=30204
#
# [3289] The Two Sneaky Numbers of Digitville
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = []
        for k, v in cnt.items():
            if v == 2:
                ans.append(k)
        return ans
# @lc code=end



#
# @lcpr case=start
# [0,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,2,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [7,1,5,4,3,4,6,0,9,5,8,2]\n
# @lcpr case=end

#

