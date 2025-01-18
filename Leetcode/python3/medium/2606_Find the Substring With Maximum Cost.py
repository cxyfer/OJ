#
# @lc app=leetcode id=2606 lang=python3
# @lcpr version=30203
#
# [2606] Find the Substring With Maximum Cost
#

# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # return self.solve1(s, chars, vals)
        return self.solve2(s, chars, vals)

    def solve1(self, s: str, chars: str, vals: List[int]) -> int:
        n = len(s)
        mp = [i + 1 for i in range(26)]
        for ch, val in zip(chars, vals):
            idx = ord(ch) - ord('a')
            mp[idx] = val
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            idx = ord(s[i - 1]) - ord('a')
            dp[i] = max(dp[i - 1] + mp[idx], mp[idx])
        return max(dp)

    def solve2(self, s: str, chars: str, vals: List[int]) -> int:
        mp = [i + 1 for i in range(26)]
        for ch, val in zip(chars, vals):
            idx = ord(ch) - ord('a')
            mp[idx] = val
        ans = 0
        f = 0
        for ch in s:
            idx = ord(ch) - ord('a')
            f = max(f + mp[idx], mp[idx])
            ans = max(ans, f)
        return ans
# @lc code=end


sol = Solution()
print(sol.maximumCostSubstring("adaa", "d", [-1000]))  # 2
print(sol.maximumCostSubstring("abc", "abc", [-1, -1, -1]))  # 0

#
# @lcpr case=start
# "adaa"\n"d"\n[-1000]\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"abc"\n[-1,-1,-1]\n
# @lcpr case=end

#
