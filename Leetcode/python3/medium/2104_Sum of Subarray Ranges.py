#
# @lc app=leetcode id=2104 lang=python3
#
# [2104] Sum of Subarray Ranges
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9) + 7
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        return (self.sumSubarrayMaxs(nums) + self.sumSubarrayMaxs([-x for x in nums]))

    # 907. Sum of Subarray Minimums 改成求 Maximums
    def sumSubarrayMaxs(self, arr: List[int]) -> int:
        n = len(arr)

        # L[i] 表示左側第一個 >= arr[i] 的位置
        # R[i] 表示右側第一個 > arr[i] 的最小位置
        L = [-1] * n
        R = [n] * n
        st = []
        for i, x in enumerate(arr):
            while st and x > arr[st[-1]]:
                R[st.pop()] = i
            st.append(i)

        st = []
        for i in range(n - 1, -1, -1):
            x = arr[i]
            while st and x >= arr[st[-1]]:
                L[st.pop()] = i
            st.append(i)

        return sum(x * (i - L[i]) * (R[i] - i) for i, x in enumerate(arr))
# @lc code=end
sol = Solution()
print(sol.subArrayRanges([1,2,3]))  # 4
print(sol.subArrayRanges([1,3,3]))  # 4
print(sol.subArrayRanges([4,-2,-3,4,1]))  # 59