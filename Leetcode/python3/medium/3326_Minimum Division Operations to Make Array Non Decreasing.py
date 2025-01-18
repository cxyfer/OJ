#
# @lc app=leetcode id=3326 lang=python3
# @lcpr version=30204
#
# [3326] Minimum Division Operations to Make Array Non Decreasing
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAX = int(1e6) + 5
LPF = [0] * (MAX + 1) # lowest prime factor
for i in range(2, MAX):
    if LPF[i] == 0:
        for j in range(i, MAX + 1, i):
            if LPF[j] == 0:
                LPF[j] = i
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                nums[i] = LPF[nums[i]]
                if nums[i] > nums[i + 1]:
                    return -1
                ans += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.minOperations([240,2,11])) # -1

#
# @lcpr case=start
# [25,7]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n
# @lcpr case=end

#

