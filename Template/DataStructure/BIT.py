from typing import *


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


# PURQ (Point Update Range Query), 0-based, initialization: O(nlogn)
class FenwickTree_PURQ1:
    __slots__ = ['tree']

    def __init__(self, n: int):  # Not Initialize with nums
        self.n = n
        self.tree = [0] * n

    def add(self, k: int, x: int) -> None:  # 令 nums[k] += x
        k += 1
        while k <= len(self.tree):
            self.tree[k - 1] += x
            k += (k & -k)

    def update(self, k: int, x: int) -> None:  # 令 nums[k] = x
        self.add(k, x - self.nums[k])
        self.nums[k] = x

    # 區間查詢 (區間求和): 求 nums[l] 到 nums[r] 之和
    def sum(self, l: int, r: int) -> int:
        if l > r:
            return 0
        return self.preSum(r) - self.preSum(l - 1)

    def preSum(self, k: int) -> int:  # 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        res = 0
        k += 1
        while k > 0:
            res += self.tree[k - 1]
            k -= (k & -k)
        return res


# PURQ (Point Update Range Query), 1-based, initialization: O(n)
class FenwickTree_PURQ2:
    __slots__ = 'nums', 'tree'

    def __init__(self, nums: List[int]):  # 下標從 1 開始
        n = len(nums)
        self.nums = nums
        tree = [0] * (n + 1)  # 下標從 1 開始
        for i, x in enumerate(nums, 1):  # initialization: O(n)
            tree[i] += x
            nxt = i + (i & -i)  # 下一個關鍵區間的右端點
            if nxt <= n:
                tree[nxt] += tree[i]
        self.tree = tree

    def add(self, k: int, x: int) -> None:  # 令 nums[k] += x
        k += 1
        while k < len(self.tree):
            self.tree[k] += x
            k += (k & -k)

    def update(self, k: int, x: int) -> None:  # 令 nums[k] = x
        self.add(k, x - self.nums[k])
        self.nums[k] = x

    # 區間查詢 (區間求和): 求 nums[l] 到 nums[r] 之和
    def sum(self, l: int, r: int) -> int:
        if l > r:
            return 0
        return self.preSum(r+1) - self.preSum(l)

    def preSum(self, k: int) -> int:  # 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        s = 0
        while k > 0:
            s += self.tree[k]
            k &= k - 1  # 等同 k -= (k & -k)
        return s
