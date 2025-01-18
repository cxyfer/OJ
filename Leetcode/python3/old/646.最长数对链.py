#
# @lc app=leetcode.cn id=646 lang=python3
#
# [646] 最长数对链
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Greedy
        cur = -math.inf # current end
        ans = 0
        pairs.sort(key=lambda x: x[1])
        for x, y in pairs:
            if x > cur:
                cur = y
                ans += 1
        return ans
# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    print(sol.findLongestChain([[1,2],[2,3],[3,4]]))