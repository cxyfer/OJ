#
# @lc app=leetcode id=3201 lang=python3
#
# [3201] Find the Maximum Length of Valid Subsequence I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = [0, 0]
        for x in nums:
            cnt[x & 1] += 1
        def f(b: int) -> int:
            res = 0
            for x in nums:
                if x & 1 == b:
                    res += 1
                    b ^= 1
            return res
        return max(f(0), f(1), cnt[0], cnt[1])

class Solution2:
    def maximumLength(self, nums: List[int]) -> int:
        return max(reduce(lambda ans, b:
                          [ans[0] + (1 - b), ans[1] + b, ans[2] + (b == (ans[2] & 1)), ans[3] + (b != (ans[3] & 1))],
                          map(lambda x: x & 1, nums),
                          [0, 0, 0, 0]))

# Solution = Solution1
Solution = Solution2
# @lc code=end