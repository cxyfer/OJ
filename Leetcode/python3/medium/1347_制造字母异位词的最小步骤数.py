#
# @lc app=leetcode.cn id=1347 lang=python3
#
# [1347] 制造字母异位词的最小步骤数
#
from preImport import *
# @lc code=start
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt1 = Counter(s)
        cnt2 = Counter(t)
        return sum([max(0, cnt1[k]-cnt2[k]) for k in cnt1.keys()])
# @lc code=end
sol = Solution()
print(sol.minSteps("bab","aba")) # 1
print(sol.minSteps("leetcode","practice")) # 5
print(sol.minSteps("anagram","mangaar")) # 0
