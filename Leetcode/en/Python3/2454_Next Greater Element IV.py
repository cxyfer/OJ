# @algorithm @lc id=2549 lang=python3 
# @title next-greater-element-iv


from en.Python3.mod.preImport import *
# @test([2,4,0,9,6])=[9,6,6,-1,-1]
# @test([3,3])=[-1,-1]
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
            size = len(st2)
            while st1 and nums[st1[-1]] < num:  # num 是**第一個**比 nums[i] 大的數
                i = st1.pop()
                st2.append(i)
            if size != len(st2): # 反轉新加入的部分
                st2[size:] = reversed(st2[size:])
            st1.append(idx)
        return ans