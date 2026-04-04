#
# @lc app=leetcode id=3886 lang=python3
#
# [3886] Sum of Sortable Integers
#


# @lcpr-template-start
from preImport import *

# @lcpr-template-end
# @lc code=start
MAX_N = int(1e5)
factors = [[] for _ in range(MAX_N + 1)]
for i in range(1, MAX_N + 1):
    for j in range(i, MAX_N + 1, i):
        factors[j].append(i)


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        def check(st: int, k: int) -> bool:
            cnt = 1
            for i in range(st + 1, st + k):
                if nums[i - 1] > nums[i]:
                    cnt += 1
                    if cnt > 2:
                        return False
            return cnt == 1 or (cnt == 2 and nums[st] >= nums[st + k - 1])

        ans = 0
        for k in reversed(factors[n]):
            pre_mx = -1
            for st in range(0, n, k):
                if not check(st, k):
                    break
                if min(nums[st : st + k]) < pre_mx:
                    break
                pre_mx = max(nums[st : st + k])
            else:
                ans += k
        return ans
# @lc code=end
