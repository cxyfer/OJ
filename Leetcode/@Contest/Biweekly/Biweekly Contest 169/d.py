import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

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
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        bit = BIT(2 * n + 1)  # [-n, n] -> [1, 2n + 1]
        offset = n + 1
        bit.add(offset, 1)
        ans = s = 0
        for i in range(n):
            s += (1 if nums[i] == target else -1)
            ans += bit.query(1, s + offset - 1)
            bit.add(s + offset, 1)
        return ans

sol = Solution()
print(sol.countMajoritySubarrays([1,2,2,3], 2))  # 5

"""

# Q4. ||枚舉右維護左||
||題意要求滿足 cnt_target > cnt_other 的子陣列數量。
在 Q2 中不難想到使用前綴和維護 cnt_target - cnt_other 的值，也就是當 s[r] - s[l - 1] > 0 時，子陣列 [l, r] 滿足題意。
那麼可以透過枚舉右端點 r，維護有多少個 s[l - 1] < s[r] 的左端點，這就是經典的求逆序對，可以通過 BIT 來維護。
注意上述前綴和的值域是 [-n, n]，需要將其做偏移。||
"""