#
# @lc app=leetcode id=1649 lang=python3
# @lcpr version=30202
#
# [1649] Create Sorted Array through Instructions
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

class FenwickTree: # PURQ (Point Update Range Query), 0-based, initialization: O(nlogn)
    __slots__ = 'tree'

    def __init__(self, n : int):
        self.tree = [0] * n

    def add(self, k: int, x: int) -> None: # 令 nums[k] += x
        k += 1
        while k <= len(self.tree):
            self.tree[k - 1] += x
            k += (k & -k)

    def preSum(self, k: int) -> int: # 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        res = 0
        k += 1
        while k > 0:
            res += self.tree[k - 1]
            k -= (k & -k)
        return res
    
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        sorted_nums = sorted(set(instructions)) # 離散化
        m = len(sorted_nums)
        bit = FenwickTree(m)
        ans = 0
        for x in instructions:
            idx = bisect_left(sorted_nums, x)
            l, r = bit.preSum(idx - 1), bit.preSum(m - 1) - bit.preSum(idx)
            ans = (ans + min(l, r)) % MOD
            bit.add(idx, 1)
        return ans
# @lc code=end

sol = Solution()
print(sol.createSortedArray([1,5,6,2])) # 1
print(sol.createSortedArray([1,2,3,6,5,4])) # 3
print(sol.createSortedArray([1,3,3,3,2,4,2,1,2])) # 4

#
# @lcpr case=start
# [1,5,6,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,6,5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,3,3,2,4,2,1,2]\n
# @lcpr case=end

#

