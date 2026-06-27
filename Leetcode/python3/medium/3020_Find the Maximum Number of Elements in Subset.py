#
# @lc app=leetcode id=3020 lang=python3
#
# [3020] Find the Maximum Number of Elements in Subset
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
枚舉 中間或兩側 的元素，則只要檢查 x/2或 2x 是否存在 cnt 即可。
注意特判 1 的情況。
"""
# @lc code=start
class Solution1a:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = (cnt[1] - 1) | 1
        del cnt[1]

        for x in cnt:
            cur = 1
            sqrt = isqrt(x)
            while sqrt * sqrt == x and cnt[sqrt] >= 2:
                cur += 2
                x = sqrt
                sqrt = isqrt(x)
            ans = max(ans, cur)
        return ans


class Solution1b:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = (cnt[1] - 1) | 1
        del cnt[1]

        for x in cnt:
            cur = 1
            while cnt[x] >= 2 and x * x in cnt:
                cur += 2
                x *= x
            ans = max(ans, cur)
        return ans


# Solution = Solution1a
Solution = Solution1b
# @lc code=end

sol = Solution()
print(sol.maximumLength([5, 4, 1, 2, 2]))  # 3
print(sol.maximumLength([1, 3, 2, 4]))  # 1
print(sol.maximumLength([1, 1, 1]))  # 3
print(sol.maximumLength([14, 14, 196, 196, 38416, 38416]))  # 5