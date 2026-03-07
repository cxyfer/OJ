#
# @lc app=leetcode id=1888 lang=python3
#
# [1888] Minimum Number of Flips to Make the Binary String Alternating
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ans = n
        cnt = 0
        for r in range(n * 2 - 1):
            # if (ord(s[r % n]) - ord('0')) != (r & 1):
            # if ord(s[r % n]) & 1 != r & 1:
            if (ord(s[r % n]) ^ r) & 1:
                cnt += 1
            if r >= n - 1:
                ans = min(ans, cnt, n - cnt)
                left = r - n + 1
                # if (ord(s[left]) - ord('0')) != (left & 1):
                # if ord(s[left]) & 1 != left & 1:
                if (ord(s[left]) ^ left) & 1:
                    cnt -= 1
        return ans
# @lc code=end

