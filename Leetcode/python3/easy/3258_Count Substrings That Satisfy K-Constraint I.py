#
# @lc app=leetcode id=3258 lang=python3
# @lcpr version=30204
#
# [3258] Count Substrings That Satisfy K-Constraint I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cnt = [0, 0]
        ans = left = 0
        for right, ch in enumerate(s):
            cnt[ord(ch) - ord("0")] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[ord(s[left]) - ord("0")] -= 1
                left += 1
            ans += right - left + 1
        return ans
# @lc code=end



#
# @lcpr case=start
# "10101"\n1\n
# @lcpr case=end

# @lcpr case=start
# "1010101"\n2\n
# @lcpr case=end

# @lcpr case=start
# "11111"\n1\n
# @lcpr case=end

#

