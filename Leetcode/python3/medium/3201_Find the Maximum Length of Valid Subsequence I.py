#
# @lc app=leetcode id=3201 lang=python3
#
# [3201] Find the Maximum Length of Valid Subsequence I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
考慮全奇、全偶、奇偶交錯(奇先、偶先)，共 4 種情況。

如果是 **奇偶交錯** 的話，則 nums[0] 一定可以出現在最長的子序列中，可以用矛盾法證明：
令 seq 為最長的子序列且不包含 nums[0]，則，
- 若 nums[0] 的奇偶性與 seq[0] 相同，則可以用 nums[0] 替換 seq[0]，子序列長度相同；
- 若 nums[0] 的奇偶性與 seq[0] 不同，則可以產生更長的子序列，產生矛盾
"""
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
        # return max(f(0), f(1), cnt[0], cnt[1])
        return max(f(nums[0] & 1), cnt[0], cnt[1])

class Solution2:
    def maximumLength(self, nums: List[int]) -> int:
        return max(reduce(lambda ans, b:
                          [ans[0] + (b ^ 1), ans[1] + b, ans[2] + (b == (ans[2] & 1)), ans[3] + (b != (ans[3] & 1))],
                          map(lambda x: x & 1, nums),
                          [0, 0, 0, 0]))

# Solution = Solution1
Solution = Solution2
# @lc code=end