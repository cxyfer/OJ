#
# @lc app=leetcode id=2275 lang=python3
# @lcpr version=30204
#
# [2275] Largest Combination With Bitwise AND Greater Than Zero
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
由於題目要求 Subsequence 的 AND 值大於 0，那麼這個 AND 值中，一定有一個 bit 是 1。

那麼我們可以枚舉這個 bit，然後計算有多少個數在這個 bit 上是 1，即可求出答案。
"""
# @lc code=start
class Solution1:
    def largestCombination(self, candidates: List[int]) -> int:
        # return max(sum((x >> b) & 1 for x in candidates) for b in range(24))
        ans = 0
        for b in range(24):
            cur = 0
            for x in candidates:
                if (x >> b) & 1:
                    cur += 1
            ans = max(ans, cur)
        return ans

class Solution2:
    def largestCombination(self, candidates: List[int]) -> int:
        cnt = [0] * 24
        for x in candidates:
            while x:
                lb = x & -x
                x -= lb
                cnt[lb.bit_length() - 1] += 1
        return max(cnt)
    
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [16,17,71,62,12,24,14]\n
# @lcpr case=end

# @lcpr case=start
# [8,8]\n
# @lcpr case=end

#

