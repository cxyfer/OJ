#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class BIT:  # PURQ, 1-based
    __slots__ = ['tree']

    def __init__(self, n : int):
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
    def reversePairs(self, nums: List[int]) -> int:
        # 離散化，注意也要把 2 * x 也加入離散化
        mp = {x: i + 1 for i, x in enumerate(sorted(set(nums + [2 * x for x in nums])))}
        # BIT
        bit = BIT(len(mp))
        ans = 0
        for i, x in enumerate(nums):
            ans += i - bit.query(1, mp[2 * x])
            bit.add(mp[x], 1)
        return ans
# @lc code=end
sol = Solution()
print(sol.reversePairs([1,3,2,3,1]))  # 2
print(sol.reversePairs([2,4,3,5,1]))  # 3
print(sol.reversePairs([-5,-5]))  # 1