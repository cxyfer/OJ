#
# @lc app=leetcode id=3768 lang=python3
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
BIT + Sliding Window

逆序對問題可以對值域維護頻率做區間查詢來解決，
本題只是將此問題放到固定大小的窗口中，額外考慮出窗口時的逆序對數量變化即可。
注意值域，需要離散化。
"""
# @lc code=start
class BIT:  # PURQ, 1-based
    __slots__ = ['tree']

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, k: int, x: int) -> None:  # 令 nums[k] += x
        while k < len(self.tree):
            self.tree[k] += x
            k += k & -k

    def preSum(self, k: int) -> int:  # 求 nums[:k+1] 之和
        res = 0
        while k > 0:
            res += self.tree[k]
            k -= (k & -k)
        return res

    def query(self, l: int, r: int) -> int:  # 求 nums[l:r+1] 之和
        if l > r:
            return 0
        return self.preSum(r) - self.preSum(l - 1)

class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        B = list(sorted(set(nums)))
        m = len(B)
        mp = {x: i for i, x in enumerate(B, start=1)}

        bit = BIT(m)
        ans = float("inf")
        cur = 0
        for r, x in enumerate(nums):
            cur += bit.query(mp[x] + 1, m)
            bit.add(mp[x], 1)
            if r >= k - 1:
                ans = min(ans, cur)
                y = nums[r - k + 1]
                cur -= bit.query(1, mp[y] - 1)
                bit.add(mp[y], -1)
        return ans
# @lc code=end

sol = Solution()
print(sol.minInversionCount([3,1,2,5,4], 3))  # 0
print(sol.minInversionCount([5,3,2,1], 4))  # 6 