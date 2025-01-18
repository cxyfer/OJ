#
# @lc app=leetcode id=3324 lang=python3
# @lcpr version=30204
#
# [3324] Find the Sequence of Strings Appeared on the Screen
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        s = []
        for ch in target:
            s.append('a')
            ans.append(''.join(s))
            for _ in range(ord(ch) - ord('a')):
                s[-1] = chr(ord(s[-1]) + 1)
                ans.append(''.join(s))
        return ans
# @lc code=end



#
# @lcpr case=start
# "abc"\n
# @lcpr case=end

# @lcpr case=start
# "he"\n
# @lcpr case=end

#

