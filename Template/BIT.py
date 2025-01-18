from typing import *

class FenwickTree_PURQ1: # PURQ (Point Update Range Query), 0-based, initialization: O(nlogn)
    __slots__ = 'nums', 'tree'

    def __init__(self, n : int): # Not Initialize with nums
        self.n = n
        self.tree = [0] * n

    # def __init__(self, nums: List[int]):
    #     n = len(nums)
    #     self.nums = nums
    #     self.tree = [0] * n
    #     for i, x in enumerate(nums): # initialization: O(nlogn)
    #         self.add(i, x)

    def add(self, k: int, x: int) -> None: # 令 nums[k] += x
        k += 1
        while k <= len(self.tree):
            self.tree[k - 1] += x
            k += (k & -k)

    def update(self, k: int, x: int) -> None: # 令 nums[k] = x
        self.add(k, x - self.nums[k])
        self.nums[k] = x

    def sum(self, l: int, r: int) -> int: # 區間查詢 (區間求和): 求 nums[l] 到 nums[r] 之和
        if l > r:
            return 0
        return self.preSum(r) - self.preSum(l - 1)

    def preSum(self, k: int) -> int: # 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        res = 0
        k += 1
        while k > 0:
            res += self.tree[k - 1]
            k -= (k & -k)
        return res

class FenwickTree_PURQ2: # PURQ (Point Update Range Query), 1-based, initialization: O(n)
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
        if l > r:
            return 0
        return self.preSum(r+1) - self.preSum(l)

    def preSum(self, k: int) -> int: # 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        s = 0
        while k > 0:
            s += self.tree[k]
            k &= k - 1 # 等同 k -= (k & -k)
        return s