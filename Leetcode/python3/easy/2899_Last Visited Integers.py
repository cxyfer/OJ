#
# @lc app=leetcode id=2899 lang=python3
#
# [2899] Last Visited Integers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        ans = []
        seen = deque()
        k = 0
        for x in nums:
            if x > 0:
                seen.appendleft(x)
                k = 0  # 題目要求的是連續的 -1 的數量，因此需要重置
            else:
                k += 1
                if k <= len(seen):
                    ans.append(seen[k - 1])
                else:
                    ans.append(-1)
        return ans
# @lc code=end

