#
# @lc app=leetcode id=719 lang=python3
# @lcpr version=30204
#
# [719] Find K-th Smallest Pair Distance
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        第 k 小 -> 二分答案(距離)
        計算距離 <= mid 的 pair 數量 -> 枚舉右界二分 / 滑動窗口
    """
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort() # 由小到大排序
        
        def check1(mid: int) -> int: # 計算距離 <= mid 的 pair 數量
            res = 0
            for j, x in enumerate(nums): # 枚舉右端點 j
                i = bisect_left(nums, x - mid, 0, j)
                res += j - i # (i, j), (i+1, j), ..., (j-1, j) 距離都小於等於 mid
            return res
        
        def check2(mid: int) -> int: # 計算距離 <= mid 的 pair 數量
            res = left = 0
            for right, x in enumerate(nums): # 枚舉右端點 right
                while x - nums[left] > mid: # 移動左端點直到滿足條件為止
                    left += 1
                res += right - left # (left, right), (left+1, right), ..., (right-1, right) 距離都小於等於 mid
            return res
        
        # 對答案做二分搜尋
        # return bisect_left(range(nums[n-1] - nums[0]), k, key=check1)
        return bisect_left(range(nums[n-1] - nums[0]), k, key=check2)
# @lc code=end

#
# @lcpr case=start
# [1,3,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,6,1]\n3\n
# @lcpr case=end

#

