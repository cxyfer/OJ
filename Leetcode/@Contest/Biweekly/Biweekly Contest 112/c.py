# 6989. Maximum Sum of Almost Unique Subarray

# You are given an integer array nums and two positive integers m and k.

# Return the maximum sum out of all almost unique subarrays of length k of nums. If no such subarray exists, return 0.

# A subarray of nums is almost unique if it contains at least m pairwise distinct elements.

# A subarray is a contiguous non-empty sequence of elements within an array.
from typing import List
from collections import Counter
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # Sliding window
        cnt = Counter(nums[:k])
        s = sum(nums[:k]) # sum of subarray
        ans = 0
        pairwise = len(cnt) # pairwise distinct elements
        if pairwise >= m:
            ans = max(ans, s)
        left = 0
        # print(cnt)
        for i in range(k, len(nums)):
            num = nums[i]
            # 移除左邊的元素
            cnt[nums[left]] -= 1
            s -= nums[left]
            if cnt[nums[left]] == 0: # 如果移除後的元素個數為0，則pairwise - 1
                pairwise -= 1
                
            # 加入右邊的元素
            cnt[num] += 1
            s += num
            if cnt[num] == 1: # 從0變成1，則pairwise + 1
                pairwise += 1
            if pairwise >= m:
                ans = max(ans, s)
            left += 1
            # print(s, pairwise, ans, cnt)
        return ans
    
sol = Solution()
# print(sol.maxSum([2,6,7,3,1,7], 3, 4)) # 18
print(sol.maxSum([5,9,9,2,4,5,4], 1, 3)) # 23