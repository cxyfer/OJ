#
# @lc app=leetcode id=2156 lang=python3
# @lcpr version=30204
#
# [2156] Find Substring With Given Hash Value
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        hs = 0
        for i in range(n - 1, n - k - 1, -1):
            d = ord(s[i]) - ord('a') + 1
            hs = (hs * power + d) % modulo
        ans = n - k if hs == hashValue else -1
        Pk = pow(power, k, modulo)
        for r in range(n - k - 1, -1, -1):
            dr = ord(s[r]) - ord('a') + 1
            dl = ord(s[r + k]) - ord('a') + 1
            hs = (hs * power + dr - Pk * dl) % modulo
            if hs == hashValue:
                ans = r
        return s[ans:ans+k]
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n7\n20\n2\n0\n
# @lcpr case=end

# @lcpr case=start
# "fbxzaad"\n31\n100\n3\n32\n
# @lcpr case=end

#

