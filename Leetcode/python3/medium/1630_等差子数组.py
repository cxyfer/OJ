#
# @lc app=leetcode.cn id=1630 lang=python3
#
# [1630] 等差子数组
#
from preImport import *
# @lc code=start
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for left, right in zip(l, r):
            mx = max(nums[left:right+1])
            mn = min(nums[left:right+1])
            if mx == mn: # 全部相等
                ans.append(True)
                continue
            if (mx-mn) % (right-left) != 0: # 公差不為整數
                ans.append(False)
                continue
            d = (mx-mn) // (right-left) # 公差
            flag = True
            for i, num in enumerate(sorted(nums[left:right+1])):
                if num != mn + d * i:
                    flag = False
                    break
            ans.append(flag)
        return ans
# @lc code=end

