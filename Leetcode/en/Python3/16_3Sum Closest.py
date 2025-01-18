# @algorithm @lc id=16 lang=python3 
# @title 3sum-closest


from en.Python3.mod.preImport import *
# @test([-1,2,1,-4],1)=2
# @test([0,0,0],1)=0
class Solution:
    """
        > 基础算法精讲 01
        # Two pointers
        Similar to 15. 3Sum
        另外維護一個變數 min_diff ，記錄最接近的三數之和

        TS: O(n log n + n^2) = O(n^2)
        SC: O(1), ignore the space of sorting
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = -1 
        min_diff = float('inf')
        nums.sort()
        # i < left < right < n
        for i in range(n-2): # 枚舉第一個數字 nums[i]
            """
                一些優化：
                1. 若 nums[i] 和前一個數字相同，則在考慮 nums[i-1] 時，就已經考慮過 nums[i] 了，故可以跳過
                2. 如果 nums[i] 和 最小的兩個數字相加之和 s 大於 target ，則後面任三個數字相加都會大於 target，和 target 的差距只會更大，故可以終止迴圈
                3. 如果 nums[i] 和 最大的兩個數字相加之和 s 小於 target ，則可以跳過 nums[i]，因為 nums[i] + nums[left] + nums[right] 只會更小，導致和 target 的差距更大。
                   注意這種情況下，枚舉 i 後面的數字仍然有可能有答案，故只需要跳過 i 即可。
            """
            if i > 0 and nums[i] == nums[i-1]: # 優化1.
                continue
            s = nums[i] + nums[i+1] + nums[i+2]
            if s > target: # 優化2.
                if s - target < min_diff: # 更新答案
                    min_diff = s - target
                    ans = s
                break
            s = nums[i] + nums[n-2] + nums[n-1]
            if s < target: # 優化3.
                if target - s < min_diff:
                    min_diff = target - s
                    ans = s
                continue
            left, right = i+1, n-1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur == target: # 等於目標值，直接返回
                    return target
                elif cur > target: # 比目標值大，右邊的數字太大，往左移
                    if cur - target < min_diff:
                        min_diff = cur - target
                        ans = cur
                    right -= 1
                else: # 比目標值小，左邊的數字太小，往右移
                    if target - cur < min_diff:
                        min_diff = target - cur
                        ans = cur
                    left += 1
        return ans