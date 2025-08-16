#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a: str, b: str) -> int:
            if a + b < b + a:
                return -1
            elif a + b > b + a:
                return 1
            else:
                return 0
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(cmp), reverse=True)
        return "".join(nums) if nums[0] != "0" else "0"
# @lc code=end

sol = Solution()
print(sol.largestNumber([10, 2]))