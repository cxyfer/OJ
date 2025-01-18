#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 多数元素 II
#
from preImport import *
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = defaultdict(int)
        ans = []
        for num in nums:
            cnt[num] += 1
            if cnt[num] == n // 3 + 1:
                ans.append(num)
        return ans
# @lc code=end
sol = Solution()
print(sol.majorityElement([3,2,3])) # [3]
print(sol.majorityElement([1])) # [1]
print(sol.majorityElement([1,2])) # [1,2]

