#
# @lc app=leetcode id=307 lang=python3
# @lcpr version=30202
#
# [307] Range Sum Query - Mutable
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

"""
    Binary Indexed Tree (Fenwick Tree, BIT) 模板題
    Reference:
     - https://iyukiyama.github.io/binary-indexed-tree/
     - https://leetcode.cn/problems/range-sum-query-mutable/solutions/2524481/dai-ni-fa-ming-shu-zhuang-shu-zu-fu-shu-lyfll/
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.bit = FenwickTree(nums)

    def update(self, index: int, val: int) -> None:
        self.bit.update(index, val)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.bit.sum(left, right)
    
class FenwickTree: # PURQ (Point Update Range Query)
    __slots__ = 'nums', 'tree'

    def __init__(self, nums: List[int]): # 下標從 1 開始
        n = len(nums)
        self.nums = nums
        tree = [0] * (n + 1) # 下標從 1 開始
        for i, x in enumerate(nums, 1): # initialization: O(n)
            tree[i] += x
            nxt = i + (i & -i) # 下一個關鍵區間的右端點
            if nxt <= n:
                tree[nxt] += tree[i]
        self.tree = tree

    def add(self, k: int, x: int) -> None: # 令 nums[k] += x
        k += 1
        while k < len(self.tree):
            self.tree[k] += x
            k += (k & -k)

    def update(self, k: int, x: int) -> None: # 令 nums[k] = x
        self.add(k, x - self.nums[k])
        self.nums[k] = x

    def sum(self, l: int, r: int) -> int: # 區間查詢 (區間求和): 求 nums[l] 到 nums[r] 之和
        return self.preSum(r+1) - self.preSum(l)

    def preSum(self, k: int) -> int: # 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        s = 0
        while k > 0:
            s += self.tree[k]
            k &= k - 1 # 等同 k -= (k & -k)
        return s
# @lc code=end



