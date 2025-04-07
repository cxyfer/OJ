#
# @lc app=leetcode id=3396 lang=python3
#
# [3396] Minimum Number of Operations to Make Elements in Array Distinct
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        st = set()
        idx = n - 1
        while idx >= 0 and nums[idx] not in st:
            st.add(nums[idx])
            idx -= 1
        return math.ceil((idx + 1) / 3)
# @lc code=end

sol = Solution()
print(sol.minimumOperations([1,2,3,4,2,3,3,5,7]))  # 2
print(sol.minimumOperations([4,5,6,4,4]))  # 2
print(sol.minimumOperations([6,7,8,9]))  # 0

