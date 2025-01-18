#
# @lc app=leetcode id=3016 lang=python3
# @lcpr version=30204
#
# [3016] Minimum Number of Pushes to Type Word II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = [0] * 26
        for ch in word:
            cnt[ord(ch) - ord('a')] += 1
        cnt.sort(reverse=True)
        ans = 0
        for i, x in enumerate(cnt):
            ans += x * (i // 8 + 1)
        return ans
# @lc code=end



#
# @lcpr case=start
# "abcde"\n
# @lcpr case=end

# @lcpr case=start
# "xyzxyzxyzxyz"\n
# @lcpr case=end

# @lcpr case=start
# "aabbccddeeffgghhiiiiii"\n
# @lcpr case=end

#

