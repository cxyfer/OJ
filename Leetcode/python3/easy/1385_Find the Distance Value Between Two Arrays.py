#
# @lc app=leetcode id=1385 lang=python3
#
# [1385] Find the Distance Value Between Two Arrays
#


# @lcpr-template-start
from preImport import *


# @lcpr-template-end
# @lc code=start
class Solution1:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for x in arr1:
            idx1 = bisect_left(arr2, x - d)
            idx2 = bisect_right(arr2, x + d) - 1
            if idx1 > idx2:
                ans += 1
        return ans


class Solution2:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        ans = i = 0
        for x in arr1:
            while i < len(arr2) and arr2[i] < x - d:
                i += 1
            if i == len(arr2) or arr2[i] > x + d:
                ans += 1
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end
