#
# @lc app=leetcode id=523 lang=python3
# @lcpr version=30203
#
# [523] Continuous Subarray Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Hash Table + Prefix Sum + 同餘定理
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        return self.solve1(nums, k)
        # return self.solve2(nums, k)
    
    def solve1(self, nums: List[int], k: int) -> bool:
        s = 0
        pos = defaultdict(int) # key: sum % k, value: first index
        pos[0] = -1 # empty array
        for i, x in enumerate(nums):
            s = (s + x) % k
            if s in pos:
                if i - pos[s] > 1:
                    return True
            else:
                pos[s] = i
        return False

    def solve2(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        pos = set()
        for i in range(2, n+1):
            pos.add(s[i-2] % k)
            if s[i] % k in pos:
                return True
        return False
# @lc code=end

sol = Solution()
print(sol.checkSubarraySum([23,2,4,6,7], 6))
print(sol.checkSubarraySum([23,2,4,6,6], 7))
#
# @lcpr case=start
# [23,2,4,6,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n13\n
# @lcpr case=end

#

