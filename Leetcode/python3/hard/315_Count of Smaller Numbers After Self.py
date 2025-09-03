#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
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
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 離散化
        mp = {x: i + 1 for i, x in enumerate(sorted(set(nums)))}
        nums = [mp[x] for x in nums]
        # BIT
        bit = BIT(len(mp))
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            ans[i] = bit.query(1, nums[i] - 1)
            bit.add(nums[i], 1)
        return ans
# @lc code=end

sol = Solution()
print(sol.countSmaller([5,2,6,1]))  # [2,1,1,0]
print(sol.countSmaller([-1]))  # [0]
print(sol.countSmaller([-1,-1]))  # [0,0]