#
# @lc app=leetcode id=3876 lang=python3
#
# [3876] Construct Uniform Parity Array II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def uniformArray(self, nums1: list[int]) -> bool:
        odds = [x for x in nums1 if x & 1]
        odds.sort()

        def check(p: int) -> bool:
            for x in nums1:
                if x & 1 == p:
                    continue
                idx = bisect_right(odds, x - 1) - 1
                if idx < 0:
                    return False
            return True

        return any(check(p) for p in range(2))

class Solution2:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1) & 1:
            return True
        cnt = [0] * 2
        for x in nums1:
            cnt[x % 2] += 1
        return cnt[0] == 0 or cnt[1] == 0

# Solution = Solution1
Solution = Solution2 
# @lc code=end

