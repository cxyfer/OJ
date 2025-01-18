from typing import List
from collections import Counter

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter(nums)
        cx = cnt.most_common(1)[0][1]
        if cx > n // 2:
            return cx * 2 - n # n - (n-cx) * 2
        else:
            return 0 if n % 2 == 0 else 1
        
sol = Solution()
print(sol.minLengthAfterRemovals([1,1,4,4,5,5])) # 0
print(sol.minLengthAfterRemovals([1,1,1,1,1,1,1,2,2])) # 5
print(sol.minLengthAfterRemovals([2,3,4,4,4])) # 1
print(sol.minLengthAfterRemovals([3,3,3,3])) # 4
print(sol.minLengthAfterRemovals([2,3,3,3])) # 2

print(sol.minLengthAfterRemovals([1,1,2])) # 1
print(sol.minLengthAfterRemovals([1,1,4,4,5,5])) # 0