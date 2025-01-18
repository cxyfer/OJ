# @algorithm @lc id=1046 lang=python3 
# @title max-consecutive-ones-iii


from en.Python3.mod.preImport import *
# @test([1,1,1,0,0,0,1,1,1,1,0],2)=6
# @test([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)=10
class Solution:
    """
        Sliding window
        將題目轉換成找一個最長的子串，使得子串中0的個數不超過k個
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        cnt = 0 # 0的個數
        ans = 0
        for right in range(n):
            if nums[right] == 0:
                cnt += 1
            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans