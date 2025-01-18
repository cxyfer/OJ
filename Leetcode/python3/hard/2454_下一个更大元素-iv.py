#
# @lc app=leetcode.cn id=2454 lang=python3
#
# [2454] 下一个更大元素 IV
#
from preImport import *
# @lc code=start
class Solution:
    """
        Monotonic stack + heap
    """
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st1 = [] # monotonic stack, decreasing
        st2 = []
        ans = [-1] * n

        for idx, num in enumerate(nums): # idx = j
            while st2 and nums[st2[-1]] < num: # num 是**第二個**比 nums[i] 大的數
                i = st2.pop()
                ans[i] = num
            st = len(st2)
            while st1 and nums[st1[-1]] < num:  # num 是**第一個**比 nums[i] 大的數
                i = st1.pop()
                st2.append(i)
            if st != len(st2): # 反轉新加入的部分
                st2[st:] = reversed(st2[st:])
            st1.append(idx)
        return ans
# @lc code=end
sol = Solution()
print(sol.secondGreaterElement([11,13,15,12,0,15,12,11,9])) # [15,15,-1,-1,12,-1,-1,-1,-1]

