#
# @lc app=leetcode id=3495 lang=python3
#
# [3495] Minimum Operations to Make Array Elements Zero
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MX = int(1e9) + 5
p = [1]
while p[-1] < MX:
    p.append(p[-1] * 4)
s = [0] * len(p)
for i, (a, b) in enumerate(pairwise(p), start=1):
    s[i] = s[i - 1] + (b - a) * i

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def f(x):
            if x == 0:
                return 0
            idx = bisect_right(p, x)
            return s[idx - 1] + (x - p[idx - 1] + 1) * idx
        return sum(math.ceil((f(r) - f(l - 1)) / 2) for l, r in queries)
# @lc code=end

sol = Solution()
print(sol.minOperations([[1,2],[2,4]]))  # 3
print(sol.minOperations([[2,6]]))  # 4
print(sol.minOperations([[1,8]]))  # 7
