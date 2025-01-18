#
# @lc app=leetcode id=1653 lang=python3
# @lcpr version=30204
#
# [1653] Minimum Deletions to Make String Balanced
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # 令 dp[i][0/1] 表示刪除某些元素後，使 s[0:i] 平衡的最大長度，且最後一個字元是 0:a 或 1:b
        n = len(s)
        a, b = 0, 0
        for ch in s:
            if ch == 'a':
                a += 1
            else:
                b = max(a, b) + 1
        return n - max(a, b)
# @lc code=end



#
# @lcpr case=start
# "aababbab"\n
# @lcpr case=end

# @lcpr case=start
# "bbaaaaabb"\n
# @lcpr case=end

#

