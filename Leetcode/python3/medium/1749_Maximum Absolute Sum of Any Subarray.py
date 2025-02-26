#
# @lc app=leetcode id=1749 lang=python3
# @lcpr version=30203
#
# [1749] Maximum Absolute Sum of Any Subarray
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
1. Kadane's Algorithm
2. Prefix Sum
  - 枚舉右端點，維護左端點
  - 維護最大最小值即可
    - 由於要取絕對值，小的前綴和不一定要在大的前綴和左側，因此直接維護最大最小值即可
"""
class Solution1a:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        f1 = [0] * (n + 1)  # 正數
        f2 = [0] * (n + 1)  # 負數
        for i, x in enumerate(nums):
            f1[i + 1] = max(f1[i] + x, x)
            f2[i + 1] = min(f2[i] + x, x)
        return max(max(f1), -min(f2))
class Solution1b:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = float("-inf")
        f1, f2 = 0, 0
        for x in nums:
            f1, f2 = max(f1 + x, x), min(f2 + x, x)
            ans = max(ans, f1, -f2)
        return ans
    
class Solution2a:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = 0
        # 枚舉右端點，維護左端點
        s = mx = mn = 0
        for x in nums:
            s += x
            ans = max(ans, mx - s, s - mn)
            mx = max(mx, s)
            mn = min(mn, s)
        return ans

class Solution2b:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = mx = mn = 0
        for x in nums:
            s += x
            mx = max(mx, s)
            mn = min(mn, s)
        return mx - mn
    
# class Solution(Solution1a):
# class Solution(Solution1b):
# class Solution(Solution2a):
class Solution(Solution2b):
    pass
# @lc code=end
sol = Solution()
print(sol.maxAbsoluteSum([1,-3,2,3,-4])) # 5
print(sol.maxAbsoluteSum([2,-5,1,-4,3,-2])) # 8

#
# @lcpr case=start
# [1,-3,2,3,-4]\n
# @lcpr case=end

# @lcpr case=start
# [2,-5,1,-4,3,-2]\n
# @lcpr case=end

#
