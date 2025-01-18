#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
from preImport import *
# @lc code=start
class Solution:
    """
        # Two pointers
        Extend from 167. Sum of Two Numbers II - Input Ordered Array
        Similar to 15. 3Sum, 改成枚舉兩個數字，然後用雙指標找另外兩個數字

        i < j < left < right < n
        TS: O(n log n + n^3) = O(n^3)
        SC: O(1), ignore the space of sorting
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n-3): # 枚舉第一個數字 nums[i]
            x = nums[i]
            """
                一些優化：
                1. 若 nums[i] 和前一個數字相同，則在考慮 nums[i-1] 時，就已經考慮過 nums[i] 了，為了避免重複答案，故可以跳過
                2. 如果 nums[i] + nums[j] 和 最小的兩個數字相加之和 s 大於 target ，則 i 後面任四個數字相加都會大於 target，故可以終止迴圈
                3. 如果 nums[i] + nums[j] 和 最大的兩個數字相加之和 s 小於 target ，則在取 i 為第一個數字時，後面得到的結果只會更小，故可以跳過 i
                   注意這種情況下，枚舉 i 後面的數字仍然有可能有答案，故只需要跳過 i 即可。
            """
            if i > 0 and x == nums[i-1]: # 優化1. 重複數字會導致重複答案，根據題意，跳過
                continue
            if x + nums[i+1] + nums[i+2] + nums[i+3] > target: # 優化2. 
                break
            if x + nums[n-3] + nums[n-2] + nums[n-1] < target: # 優化3.
                continue
            for j in range(i+1, n-2): # 枚舉第二個數字 nums[j]
                y = nums[j]
                if j > i+1 and y == nums[j-1]: # 優化1. 重複數字會導致重複答案，根據題意，跳過
                    continue
                if x + y + nums[j+1] + nums[j+2] > target: # 優化2.
                    break
                if x + y + nums[n-2] + nums[n-1] < target: # 優化3.
                    continue
                left, right = j+1, n-1
                while left < right:
                    cur = x + y + nums[left] + nums[right]
                    if cur > target:
                        right -= 1
                    elif cur < target:
                        left += 1
                    else: 
                        ans.append([x, y, nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]: # 避免重複答案，跳過
                            left += 1
                        while left < right and nums[right] == nums[right-1]: # 避免重複答案，跳過
                            right -= 1
                        # 找下一個答案
                        left += 1
                        right -= 1
        return ans
# @lc code=end
sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2],0)) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]] 
print(sol.fourSum([2,2,2,2,2],8)) # [[2,2,2,2]]