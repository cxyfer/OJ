#
# @lc app=leetcode id=2582 lang=python3
# @lcpr version=30204
#
# [2582] Pass the Pillow
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        k = 2 * (n - 1) # 傳遞一圈的時間
        r = time % k
        return 1 + r if r < n else n - (r - (n - 1))
# @lc code=end



#
# @lcpr case=start
# 4\n5\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

#

