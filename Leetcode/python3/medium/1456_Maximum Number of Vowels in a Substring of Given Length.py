#
# @lc app=leetcode id=1456 lang=python3
# @lcpr version=30204
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = have = 0
        for right, ch in enumerate(s):
            have += ch in "aeiou"
            if right < k - 1:
                continue
            ans = max(ans, have)
            have -= s[right - k + 1] in "aeiou"
        return ans
# @lc code=end



#
# @lcpr case=start
# "abciiidef"\n3\n
# @lcpr case=end

# @lcpr case=start
# "aeiou"\n2\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n3\n
# @lcpr case=end

#

