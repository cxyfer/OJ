#
# @lc app=leetcode.cn id=2125 lang=python3
#
# [2125] 银行中的激光束数量
#
from preImport import *
# @lc code=start
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        cnt = [line.count('1') for line in bank]
        ans = 0
        pre = 0
        for x in cnt:
            if x > 0:
                ans += pre * x
                pre = x
        return ans
# @lc code=end
sol = Solution()
print(sol.numberOfBeams(["011001","000000","010100","001000"])) # 8
print(sol.numberOfBeams(["000","111","000"])) # 0