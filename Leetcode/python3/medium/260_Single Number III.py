#
# @lc app=leetcode id=260 lang=python3
# @lcpr version=30203
#
# [260] Single Number III
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. Hash Table
        2. Bit Manipulation
    """
    def singleNumber(self, nums: List[int]) -> List[int]:
        return self.solve1(nums)
        # return self.solve2(nums)
    def solve1(self, nums: List[int]) -> List[int]:
        # return [k for k, v in Counter(nums).items() if v == 1]
        cnt = Counter(nums)
        ans = []
        for k, v in cnt.items():
            if v == 1:
                ans.append(k)
        return ans
    def solve2(self, nums: List[int]) -> List[int]:
        xor = 0
        for x in nums:
            xor ^= x
        lb = xor & -xor # 最低位的 1
        ans = [0, 0]
        for x in nums:
            ans[x & lb == 0] ^= x # 分組異或
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,1,3,2,5]\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

#

