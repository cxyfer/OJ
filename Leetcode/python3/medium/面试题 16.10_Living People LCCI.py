#
# @lc app=leetcode.cn id=面试题 16.10 lang=python3
# @lcpr version=30204
#
# [面试题 16.10] 生存人数
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        max_y = max(death)
        diff = [0] * (max_y + 2)
        for st, ed in zip(birth, death):
            diff[st] += 1
            diff[ed + 1] -= 1
        ans = mx = s = 0
        for i in range(max_y + 1):
            s += diff[i]
            if s > mx:
                ans, mx = i, s
        return ans
# @lc code=end



#
# @lcpr case=start
# [1900, 1901\n[1948, 1951, 2000]\n
# @lcpr case=end

#

