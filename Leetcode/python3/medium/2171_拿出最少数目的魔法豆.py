#
# @lc app=leetcode.cn id=2171 lang=python3
#
# [2171] 拿出最少数目的魔法豆
#
from preImport import *
# @lc code=start
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        beans.sort()
        s = list(accumulate(beans, initial=0))
        ans = s[n]
        for i, b in enumerate(beans):
            p1 = s[i] # < b 的全部拿出
            p2 = s[n] - s[i+1] - b * (n - i - 1) # > b 的減到 b
            ans = min(ans, p1 + p2)
        return ans
# @lc code=end
sol = Solution()
print(sol.minimumRemoval([4,1,6,5])) # 4
print(sol.minimumRemoval([2,10,3,2])) # 7
