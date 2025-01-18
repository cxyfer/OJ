from typing import List

class Solution:
    """
        a ^ b = c => a ^ c = b
    """
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        x, y = 0, 1
        while not abs(x-y) <= min(x, y):
            res, y = maximumXor(nums)
    def maximumXor(self, nums: List[int]) -> int:
        mask = 0
        ans = 0
        for b in range(31, -1, -1):
            mask |= 1 << b
            s = set()
            for x in nums:
                s.add(x & mask)
            candidate = ans | (1 << b)
            for prefix in s:
                x = prefix ^ candidate
                if candidate ^ prefix in s:
                    ans = candidate
                    break
        return (ans, x)
sol = Solution()
print(sol.maximumStrongPairXor([1,2,3,4,5])) # 7
print(sol.maximumStrongPairXor([10,100])) # 0
print(sol.maximumStrongPairXor([5,6,25,30])) # 7
print(sol.maximumStrongPairXor([1,2,2,1,2])) # 3
        