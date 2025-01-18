#
# @lc app=leetcode id=2905 lang=python3
# @lcpr version=30202
#
# [2905] Find Indices With Index and Value Difference II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        max_idx = min_idx = 0 # 維護最大值和最小值的 index
        for j in range(indexDifference, n): # 枚舉右指針
            i = j - indexDifference # 左指針，與右指針相差 indexDifference
            # 更新 max_idx, min_idx
            if nums[i] > nums[max_idx]:
                max_idx = i
            elif nums[i] < nums[min_idx]:
                min_idx = i
            # 判斷是否符合條件
            if nums[max_idx] - nums[j] >= valueDifference:
                return [max_idx, j]
            if nums[j] - nums[min_idx] >= valueDifference:
                return [min_idx, j]
        return [-1, -1]
# @lc code=end



#
# @lcpr case=start
# [5,1,4,1]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n0\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n2\n4\n
# @lcpr case=end

#

