# @algorithm @lc id=1918 lang=python3 
# @title maximum-score-of-a-good-subarray


from en.Python3.mod.preImport import *
# @test([1,4,3,7,4,5],3)=15
# @test([5,5,4,5,4,1,1,1],0)=20
class Solution:
    """
        Monotonic stack
    """
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = [] # monotonic stack, top is the smallest element
        ans = 0
        for i, num in enumerate(nums):
            while st and num < nums[st[-1]]:
                idx = st.pop() # index of the smallest element 
                l_idx = 0 if not st else st[-1] + 1
                r_idx = i - 1
                if l_idx <= k <= r_idx:
                    ans = max(ans, nums[idx] * (r_idx - l_idx + 1))
            st.append(i)
        while st:
            idx = st.pop()
            l_idx = 0 if not st else st[-1] + 1
            r_idx = n - 1
            if l_idx <= k <= r_idx:
                ans = max(ans, nums[idx] * (r_idx - l_idx + 1))
        return ans