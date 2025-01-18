from typing import List
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        idx = nums.index(min(nums))
        for i in range(n-1):
            if nums[(idx + i) % n] > nums[(idx + i + 1) % n]:
                return -1
        return (n - idx) % n

sol = Solution()
print(sol.minimumRightShifts([3,4,5,1,2]))
print(sol.minimumRightShifts([1,3,5]))
print(sol.minimumRightShifts([2,1,4]))