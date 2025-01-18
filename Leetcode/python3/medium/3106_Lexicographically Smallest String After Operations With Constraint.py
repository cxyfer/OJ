#
# @lc app=leetcode id=3106 lang=python3
# @lcpr version=30204
#
# [3106] Lexicographically Smallest String After Operations With Constraint
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Greedy
        盡可能讓前面的字串改成 'a'，這樣字典序會最小
        當剩餘額度不足的時候，就往前改
        Time: O(n)
    """
    def getSmallestString(self, s: str, k: int) -> str:
        s = list(s)
        for i, ch in enumerate(s):
            dis = min(ord(ch) - ord('a'), ord('z') - ord(ch) + 1)
            if dis > k: # 不足以改成 'a'，就往前改
                s[i] = chr(ord(ch) - k)
                break
            s[i] = 'a'
            k -= dis
        return ''.join(s)
# @lc code=end



#
# @lcpr case=start
# "zbbz"\n3\n
# @lcpr case=end

# @lcpr case=start
# "xaxcd"\n4\n
# @lcpr case=end

# @lcpr case=start
# "lol"\n0\n
# @lcpr case=end

#

