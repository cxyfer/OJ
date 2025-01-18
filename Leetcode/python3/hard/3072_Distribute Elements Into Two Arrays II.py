#
# @lc app=leetcode id=3072 lang=python3
# @lcpr version=30202
#
# [3072] Distribute Elements Into Two Arrays II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

"""
    1. Simulation + Binary Search
        每次查找跟插入都是 O(logn)，總共是 O(nlogn)
    2. Binary Indexed Tree (Fenwick Tree, BIT)
        Similar to 307. Range Sum Query - Mutable
        可以從模板修改而來，刪除初始化、update 方法、sum 方法
    3. SortedList
        只有 Python 可以用的方法，不過速度應該是最快的
"""

class Solution1:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1, arr2 = [nums[0]], [nums[1]] # ans
        v1, v2 = [nums[0]], [nums[1]] # sorted array

        for x in nums[2:]:
            idx1, idx2 = bisect_right(v1, x), bisect_right(v2, x)
            gc1, gc2 = len(arr1) - idx1, len(arr2) - idx2
            if gc1 > gc2 or gc1 == gc2 and len(arr1) <= len(arr2):
                arr1.append(x)
                v1.insert(idx1, x) # 用前面Binary Search的結果插入
            else:
                arr2.append(x)
                v2.insert(idx2, x)
        return arr1 + arr2
    
class FenwickTree: # PURQ (Point Update Range Query), 0-based, initialization: O(nlogn)
    __slots__ = 'tree'

    def __init__(self, n: int): # 下標從 0 開始
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

class Solution2:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sorted_nums = sorted(set(nums)) # 離散化
        m = len(sorted_nums)
        arr1, arr2 = [nums[0]], [nums[1]]
        bit1, bit2 = FenwickTree(m + 1), FenwickTree(m + 1)
        bit1.add(bisect_left(sorted_nums, nums[0]), 1)
        bit2.add(bisect_left(sorted_nums, nums[1]), 1)
        for i in range(2, n):
            v = bisect_left(sorted_nums, nums[i])
            gc1 = len(arr1) - bit1.preSum(v) # bit1.preSum(v) 表示 <= v 的元素個數，故 len(arr1) - bit1.preSum(v) 表示 > v 的元素個數
            gc2 = len(arr2) - bit2.preSum(v)
            if gc1 > gc2 or (gc1 == gc2 and len(arr1) <= len(arr2)):
                arr1.append(nums[i])
                bit1.add(v, 1)
            else:
                arr2.append(nums[i])
                bit2.add(v, 1)
        return arr1 + arr2

from sortedcontainers import SortedList

class Solution3:
    def resultArray(self, nums: List[int]) -> List[int]:
        sl1, sl2 = SortedList([nums[0]]), SortedList([nums[1]])
        res1, res2 = [nums[0]], [nums[1]]

        for x in nums[2:]:
            gc1 = len(sl1) - sl1.bisect_right(x)
            gc2 = len(sl2) - sl2.bisect_right(x)
            if gc1 > gc2 or gc1 == gc2 and len(sl1) <= len(sl2):
                sl1.add(x)
                res1.append(x)
            else:
                sl2.add(x)
                res2.append(x)
        return res1 + res2
    
class Solution(Solution3):
    pass
# @lc code=end

#
# @lcpr case=start
# [2,1,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,14,3,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3]\n
# @lcpr case=end

#

