#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from preImport import *
# @lc code=start
class Solution:
    """
        Binary search

        注意循環不變量：
        - left - 1 的回答一定為「是」
        - right + 1 的回答一定為「否」
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums: List[int], target: int) -> int: # find the leftmost target
            n = len(nums)
            left, right = 0, n - 1 # [left, right]
            while left <= right: # 區間不為空
                # mid = left + (right - left) // 2
                mid = (left + right) // 2 
                if nums[mid] < target: # 詢問：nums[mid] < target ? 
                    left = mid + 1 # [mid+1, right]
                else: 
                    right = mid - 1 # [left, mid-1]
            return left # or right+1
 
        st = find_left(nums, target)
        if st >= len(nums) or nums[st] != target: # target 不在 nums 中
            return [-1, -1]
        ed = find_left(nums, target+1) - 1
        return [st, ed]
# @lc code=end
sol = Solution()
print(sol.searchRange([5,7,7,8,8,10],8)) #[3,4]
print(sol.searchRange([5,7,7,8,8,10],6)) #[-1,-1]
print(sol.searchRange([],0)) #[-1,-1]

