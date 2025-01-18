#
# @lc app=leetcode.cn id=2366 lang=python3
#
# [2366] 将数组排序的最少替换次数
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        """
        Greedy
        1. 拆分後只能讓數字變小，不能變大，所以最後一個數字一定是拆分後的最大值
        2. 從後往前遍歷，每次拆分都是讓最大值變小，直到小於當前的最小值m
        3. 假設拆分出x個數字，所以nums[i] <= mx，而拆分次數為k = x -1
           舉例來說，nums[i] = 10, m = 3，則x = 4，拆分後為[3,3,2,2]，k = 3
        4. x >= ceil(nums[i] / m)，為使x最小取等號，x = ceil(nums[i] / m)
           k = x - 1 = ceil(nums[i] / m) - 1 = (nums[i] - 1) // m 
        5. 為了使拆分後的數字盡可能的大，拆分出的最小數字m = floor(nums[i] / x)
        """
        # 拆分
        ans, m = 0, nums[-1]
        for num in reversed(nums):
            k = math.ceil(num / m) - 1
            ans += k
            m = num // (k + 1)
        return ans

# @lc code=end

sol = Solution()
print(sol.minimumReplacement([3,9,3]))
print(sol.minimumReplacement([1,2,3,4,5]))
