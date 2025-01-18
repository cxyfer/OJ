#
# @lc app=leetcode.cn id=3034 lang=python3
#
# [3034] 匹配模式数组的子数组数目 I
#
from preImport import *
# @lc code=start
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
# @lc code=end
sol = Solution()
print(sol.countMatchingSubarrays([1,2,3,4,5,6],[1,1])) # 4
print(sol.countMatchingSubarrays([1,4,4,1,3,5,5,3],[1,0,-1])) # 2
