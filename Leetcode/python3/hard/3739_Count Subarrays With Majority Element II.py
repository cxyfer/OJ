#
# @lc app=leetcode id=3739 lang=python3
#
# [3739] Count Subarrays With Majority Element II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class BIT:  # PURQ, 1-based
    __slots__ = ["tree"]

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
            k -= k & -k
        return res

    def query(self, l: int, r: int) -> int:  # 求 nums[l:r+1] 之和
        if l > r:
            return 0
        return self.preSum(r) - self.preSum(l - 1)


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        bit = BIT(2 * n + 1)  # [-n, n] -> [1, 2n + 1]
        offset = n + 1
        bit.add(offset, 1)
        ans = s = 0
        for x in nums:
            s += 1 if x == target else -1
            ans += bit.query(1, s + offset - 1)
            bit.add(s + offset, 1)
        return ans
# @lc code=end

