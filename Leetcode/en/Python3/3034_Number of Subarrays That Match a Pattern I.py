# @algorithm @lc id=3269 lang=python3 
# @title number-of-subarrays-that-match-a-pattern-i


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5,6],[1,1])=4
# @test([1,4,4,1,3,5,5,3],[1,0,-1])=2
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        m, n = len(nums), len(pattern)
        ans = 0
        for i in range(m - n):
            flag = True
            # print(i, i + 1 + n, nums[i:i+1+n])
            for j in range(n):
                if nums[i + j] == nums[i + 1 + j]:
                    tmp = 0
                elif nums[i + j] < nums[i + 1 + j]:
                    tmp = 1
                else:
                    tmp = -1
                if pattern[j] != tmp:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans