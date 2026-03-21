#
# @lc app=leetcode id=3872 lang=python3
#
# [3872] Longest Arithmetic Sequence After Changing At Most One Element
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [y - x for x, y in pairwise(nums)]
        segs = []
        tot = 0
        for d, lst in groupby(diff):
            ln = len(list(lst))
            segs.append((d, tot, tot + ln))
            tot += ln
        ans = max(e - s + 2 for _, s, e in segs)
        m = len(segs)
        for i, (d, s, e) in enumerate(segs):
            # 改 s - 1
            if s - 2 >= 0:
                # 可以讓 [s-2, s] 成為等差數列
                if nums[s] - nums[s - 2] == d * 2:
                    ans = max(ans, e - (s - 2) + 1)
                    # 可以繼續延伸到 s-3 所屬的 seg
                    idx = i - 1
                    while idx >= 0 and s - 3 < segs[idx][1]:
                        idx -= 1
                    if idx >= 0 and segs[idx][0] == d:
                        ans = max(ans, e - segs[idx][1] + 1)
            # 改 e + 1
            if e + 2 < n:
                # 可以讓 [e, e+2] 成為等差數列
                if nums[e + 2] - nums[e] == d * 2:
                    ans = max(ans, (e + 2) - s + 1)
                    # 可以繼續延伸到 e + 3 所屬的 seg
                    idx = i + 1
                    while idx < m and e + 3 > segs[idx][2]:
                        idx += 1
                    if idx < m and segs[idx][0] == d:
                        ans = max(ans, segs[idx][2] - s + 1)
        return min(ans, n)
# @lc code=end

sol = Solution()
print(sol.longestArithmetic([9,7,5,10,1]))  # 5
print(sol.longestArithmetic([1,2,6,7]))  # 3
print(sol.longestArithmetic([9,7,5,10,1,-1,-3]))  # 7
print(sol.longestArithmetic([79734,13414,52866,11223,46264,42963]))  # 4
print(sol.longestArithmetic([45318,41616,88168,34212,96417,26808,23106,67752,15702]))  # 4
