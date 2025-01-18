#
# @lc app=leetcode id=3218 lang=python3
# @lcpr version=30204
#
# [3218] Minimum Cost for Cutting Cake I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        貪心
        注意到每做了一次橫切/縱切，之後縱切/橫切時都要多切一刀
        故越後切的位置需要切越多刀，
        因此基於貪心，越大的橫切/縱切應該越早切。
    """
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        m, n = len(horizontalCut), len(verticalCut)
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        i, j = 0, 0
        ans = 0
        while i < m or j < n:
            if i < m and (j == n or horizontalCut[i] > verticalCut[j]):
                ans += horizontalCut[i] * (j + 1)
                i += 1
            else:
                ans += verticalCut[j] * (i + 1)
                j += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# 3\n2\n[1,3]\n[5]\n
# @lcpr case=end

# @lcpr case=start
# 2\n2\n[7]\n[4]\n
# @lcpr case=end

#

