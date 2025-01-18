#
# @lc app=leetcode id=2191 lang=python3
# @lcpr version=30204
#
# [2191] Sort the Jumbled Numbers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(x):
            res = 0
            d = 1
            if x == 0:
                return mapping[0]
            while x:
                res += mapping[x % 10] * d
                x //= 10
                d *= 10
            return res
        return [x for _, _, x in sorted([(convert(x), i, x) for i, x in enumerate(nums)])]
# @lc code=end

sol = Solution()
print(sol.sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38]))
print(sol.sortJumbled([0,1,2,3,4,5,6,7,8,9], [789,456,123]))

#
# @lcpr case=start
# [8,9,4,0,2,1,3,5,7,6]\n[991,338,38]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,3,4,5,6,7,8,9]\n[789,456,123]\n
# @lcpr case=end

#

