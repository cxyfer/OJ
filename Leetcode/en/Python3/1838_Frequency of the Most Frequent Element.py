# @algorithm @lc id=1966 lang=python3 
# @title frequency-of-the-most-frequent-element


from en.Python3.mod.preImport import *
# @test([1,2,4],5)=3
# @test([1,4,8,13],5)=2
# @test([3,9,6],2)=1
class Solution:
    """
        Binary Search + Sort + Prefix Sum + Sliding Window
        二分查找答案
    """
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        presum = [0] + list(accumulate(nums))
        
        # Sliding Window
        # 檢查是否可以讓n個數字都變成nums[j]，且操作次數<=k
        def check(length): 
            for i in range(n+1-length):
                j = i + length - 1 # [i, j]
                cur = presum[j + 1] - presum[i] #
                t = nums[j] * length # target
                if t - cur <= k: # 可以讓n個數字都變成nums[j]
                    return True
            return False
        
        ans = 1 
        left, right = 1, n # 答案範圍[1, n]
        while left <= right: # [left, right]
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        return right