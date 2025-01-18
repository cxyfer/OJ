#
# @lc app=leetcode id=2962 lang=python3
# @lcpr version=30204
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. Prefix sum + Binary search
    2. Sliding window
"""
class Solution1:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = max(nums)

        pre = [0] # prefix sum
        for num in nums:
            pre.append(pre[-1] + (num == mx))
        ans = 0

        for i in range(n): # 對於每個 i，找到 pre[i] + k 的位置
            j = bisect_left(pre, pre[i] + k)
            ans += n - (j - 1)
        return ans
    
class Solution2:
    def countSubarrays(self, nums: List[int], k: int) -> int: 
        n = len(nums)
        mx = max(nums)
        ans = left = cnt = 0
        for right, x in enumerate(nums):
            if x == mx:
                cnt += 1
            while cnt == k:
                if nums[left] == mx:
                    cnt -= 1
                left += 1
            ans += left
        return ans
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end
#
# @lcpr case=start
# [1,3,2,3,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,1]\n3\n
# @lcpr case=end

#

