#
# @lc app=leetcode id=3158 lang=python3
# @lcpr version=30203
#
# [3158] Find the XOR of Numbers Which Appear Twice
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. Counter 兩次遍歷
        2. Bit Manipulation 一次遍歷
            - nums[i] <= 50 且 不是出現一次就是出現兩次
    """
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        # return self.solve1(nums)
        return self.solve2(nums)
    def solve1(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for k, v in cnt.items():
            if v == 2:
                ans ^= k
        return ans
    def solve2(self, nums: List[int]) -> int:
        ans = 0
        st = 0
        for x in nums:
            if st & (1 << x):
                ans ^= x
            else:
                st |= (1 << x)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

#

