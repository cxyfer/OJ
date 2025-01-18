# You are given a 0-indexed integer array nums.

# You can perform any number of operations, where each operation involves selecting a subarray of the array and replacing it with the sum of its elements. For example, if the given array is [1,3,5,6] and you select subarray [3,5] the array will convert to [1,8,6].

# Return the maximum length of a non-decreasing array that can be made after applying operations.

# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List
from itertools import accumulate

class Solution:
    """
        錯誤思路：Greedy (x)
        - 1, 2, 1, 3, 3
            - 1, 2, 7 (X)
            - 1, 3 ,3, 3 (O)
        找到第一個數字
    """
    def findMaximumLength(self, nums: List[int]) -> int:
        n= len(nums)
        ans, Sum = 0, 0
        pre_sum = list(accumulate(nums)) # prefix sum
        for i in range(n): # 第一個數字是前i個數字的和
            st = pre_sum[i] # 第一個數字
            temp = 1
            j = i + 1
    
            while(j < n):
                count = 0
                k = j
                while(k < n and count < st):
                    count += nums[k]
                    k += 1
    
                if(count >= st):
                    st = count
                    temp += 1
                j = k
            ans = max(ans, temp) # 更新答案
        return ans
 

    
sol = Solution()
# print(sol.findMaximumLength([5,2,2])) # 1
# print(sol.findMaximumLength([1,2,3,4])) # 4
# print(sol.findMaximumLength([4,3,2,6])) # 3
print(sol.findMaximumLength([272,482,115,925,983])) # 4