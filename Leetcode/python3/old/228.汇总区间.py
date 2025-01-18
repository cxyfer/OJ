#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Two pointers
        n = len(nums)
        left = 0
        ans = []
        for right in range(1, n+1): # right = n+1 時，輸出未處理的結果
            if right < n and nums[right] == nums[right-1] + 1:
                continue
            if left == right-1:
                ans.append(str(nums[left]))
            else:
                ans.append(f"{nums[left]}->{nums[right-1]}")
            left = right
        return ans
# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    print(sol.summaryRanges([0,1,2,4,5,7]))
    print(sol.summaryRanges([0,2,3,4,6,8,9]))
