#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(Counter(arr).values())
        return all(cnt[i] == 1 for i in cnt)
# @lc code=end

sol = Solution()
print(sol.uniqueOccurrences([1,2,2,1,1,3]))
print(sol.uniqueOccurrences([1,2]))
print(sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))