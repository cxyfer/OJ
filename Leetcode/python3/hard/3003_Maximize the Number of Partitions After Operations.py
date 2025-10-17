#
# @lc app=leetcode id=3003 lang=python3
#
# [3003] Maximize the Number of Partitions After Operations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def dfs(i: int, msk: int, changed: bool) -> int:
            if i == n:
                return 1 if msk.bit_count() <= k else 0
            c = ord(s[i]) - ord('a')
            # 不修改
            nmsk = msk | (1 << c)
            if nmsk.bit_count() <= k:
                res = dfs(i + 1, nmsk, changed)
            else:
                res = dfs(i + 1, (1 << c), changed) + 1
            # 修改
            if not changed:
                for j in range(26):
                    if j == c:
                        continue
                    nmsk = msk | (1 << j)
                    if nmsk.bit_count() <= k:
                        res = max(res, dfs(i + 1, nmsk, True))
                    else:
                        res = max(res, dfs(i + 1, (1 << j), True) + 1)
            return res
        return dfs(0, 0, False)
# @lc code=end

sol = Solution()
print(sol.maxPartitionsAfterOperations("accca", 2))  # 3
print(sol.maxPartitionsAfterOperations("aabaab", 3))  # 1
print(sol.maxPartitionsAfterOperations("xxyz", 1))  # 4
print(sol.maxPartitionsAfterOperations("aabcacc", 2))  # 3

"""
aabcacc
"""