# @algorithm @lc id=330 lang=python3 
# @title patching-array


from en.Python3.mod.preImport import *
# @test([1,3],6)=1
# @test([1,5,10],20)=2
# @test([1,2,2],5)=0
class Solution:
    """
        由小到大構造
        令 s 表示當前可以構造的最大值，則 s+1 為下一個要構造的值
        Similar to 1798. Maximum Number of Consecutive Values You Can Make
        Same to 2952. Minimum Number of Coins to be Added
    """
    def minPatches(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans, idx, s = 0, 0, 0
        
        while s < target:
            if idx < n and nums[idx] <= s + 1:
                s += nums[idx]  # 可以構造出 [0, s + nums[idx] ] 中的所有整數
                idx += 1
                continue
            else: # 因為後面的硬幣都 > s+1 ，所以無法構造出 s+1 了，需要補充 s+1
                s += s + 1
                ans += 1
        return ans