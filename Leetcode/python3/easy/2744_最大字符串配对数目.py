#
# @lc app=leetcode.cn id=2744 lang=python3
#
# [2744] 最大字符串配对数目
#
from preImport import *
# @lc code=start
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        cnt = Counter()
        for w in words:
            ans += cnt[w]
            cnt[w[::-1]] += 1
        return ans
# @lc code=end
sol = Solution()
print(sol.maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"])) # 2
print(sol.maximumNumberOfStringPairs(["ab","ba","cc"])) # 1
print(sol.maximumNumberOfStringPairs(["aa","ab"])) # 0

