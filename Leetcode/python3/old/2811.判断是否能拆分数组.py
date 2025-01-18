#
# @lc app=leetcode.cn id=2811 lang=python3
#
# [2811] 判断是否能拆分数组
#

# @lc code=start
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        # Check if it is possible to split array
        # 只要中間有兩個數字相加大於等於m，就一定可以向左右拆分
        for i in range(n-1):
            if nums[i] + nums[i+1] >= m:
                return True
        return False
# @lc code=end

