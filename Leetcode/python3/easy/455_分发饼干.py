#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#
from preImport import *
# @lc code=start
class Solution:
    """
        Greedy
    """
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m, n = len(g), len(s)
        g.sort()
        s.sort()
        ans = 0
        i = j = 0
        while i < m and j < n:
            if g[i] <= s[j]:
                i += 1
                ans += 1
            j += 1
        return ans
# @lc code=end
sol = Solution()

print(sol.findContentChildren([10,9,8,7],[5,6,7,8])) # 2