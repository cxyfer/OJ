#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        # Using fast and slow pointers
        fast, slow = 0, 0
        while fast < n:
            if nums[fast] != val:
                nums[slow] = nums[fast] 
                slow += 1
            fast += 1
        return slow
# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    print(sol.removeElement([3,2,2,3], 3))