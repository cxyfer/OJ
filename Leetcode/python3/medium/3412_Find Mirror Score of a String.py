#
# @lc app=leetcode id=3412 lang=python3
# @lcpr version=30204
#
# [3412] Find Mirror Score of a String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def calculateScore(self, s: str) -> int:
        def mirror(ch):
            return chr(ord('a') + (ord('z') - ord(ch)))

        ans = 0
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            m = mirror(ch)
            if pos[m]:
                ans += i - pos[m].pop()
            else:
                pos[ch].append(i)
        return ans
# @lc code=end



#
# @lcpr case=start
# "aczzx"\n
# @lcpr case=end

# @lcpr case=start
# "abcdef"\n
# @lcpr case=end

#

