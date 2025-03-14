#
# @lc app=leetcode id=1151 lang=python3
#
# [1151] Minimum Swaps to Group All 1's Together
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        tot = data.count(1)
        ans = tot
        cnt = left = 0
        for right, x in enumerate(data):
            cnt += x
            if right >= tot:
                cnt -= data[left]
                left += 1
            if right + 1>= tot:
                ans = min(ans, tot - cnt)
        return ans
# @lc code=end

