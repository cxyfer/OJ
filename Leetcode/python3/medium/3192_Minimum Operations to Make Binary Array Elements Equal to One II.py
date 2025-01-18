#
# @lc app=leetcode id=3192 lang=python3
# @lcpr version=30204
#
# [3192] Minimum Operations to Make Binary Array Elements Equal to One II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if x == 0: # 若前面翻轉偶數次，則需要再翻轉一次
                ans += (ans % 2 == 0)
            else: # 若前面翻轉奇數次，則需要再翻轉一次
                ans += (ans % 2 == 1)
        return ans
# @lc code=end



#
# @lcpr case=start
# [0,1,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,0,0]\n
# @lcpr case=end

#

