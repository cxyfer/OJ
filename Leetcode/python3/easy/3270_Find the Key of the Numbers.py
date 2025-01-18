#
# @lc app=leetcode id=3270 lang=python3
# @lcpr version=30204
#
# [3270] Find the Key of the Numbers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1 = str(num1).zfill(4)
        s2 = str(num2).zfill(4)
        s3 = str(num3).zfill(4)
        ans = [""] * 4
        for i in range(4):
            ans[i] = min(s1[i], s2[i], s3[i])
        return int("".join(ans))
# @lc code=end



#
# @lcpr case=start
# 1\n10\n1000\n
# @lcpr case=end

# @lcpr case=start
# 987\n879\n798\n
# @lcpr case=end

# @lcpr case=start
# 1\n2\n3\n
# @lcpr case=end

#

