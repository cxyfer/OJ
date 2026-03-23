#
# @lc app=leetcode id=3875 lang=python3
#
# [3875] Construct Uniform Parity Array I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def uniformArray(self, nums1: list[int]) -> bool:
        cnt = [0, 0]
        for x in nums1:
            cnt[x & 1] += 1

        def check(p: int) -> bool:
            for x in nums1:
                if x & 1 == p:
                    continue
                if cnt[1] - (x & 1) == 0:
                    return False
            return True

        return any(check(p) for p in range(2))

class Solution2:
    def uniformArray(self, _: list[int]) -> bool:
        return True

# Solution = Solution1
Solution = Solution2
# @lc code=end

