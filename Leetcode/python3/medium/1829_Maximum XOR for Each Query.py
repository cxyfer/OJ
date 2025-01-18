#
# @lc app=leetcode id=1829 lang=python3
# @lcpr version=30204
#
# [1829] Maximum XOR for Each Query
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        # s = [0] * (n + 1)
        # for i in range(n):
        #     s[i + 1] = s[i] ^ nums[i]
        ans = [0] * n
        s = 0
        for i, x in enumerate(nums):
            s ^= x
            ans[n - i - 1] = ((1 << maximumBit) - 1) ^ s
        return ans
        
# @lc code=end

sol = Solution()
print(sol.getMaximumXor([0,1,1,3], 2))

#
# @lcpr case=start
# [0,1,1,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,5,7]\n3\n
# @lcpr case=end

#

