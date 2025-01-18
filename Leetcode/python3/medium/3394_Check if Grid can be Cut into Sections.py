#
# @lc app=leetcode id=3394 lang=python3
# @lcpr version=30204
#
# [3394] Check if Grid can be Cut into Sections
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xPlus, yPlus = defaultdict(int), defaultdict(int)
        xMinus, yMinus = defaultdict(int), defaultdict(int)
        for x1, y1, x2, y2 in rectangles:
            xPlus[x1] += 1
            xMinus[x2] += 1
            yPlus[y1] += 1
            yMinus[y2] += 1
        
        def check(plus, minus):
            res = cur = 0
            keys = set(plus.keys()) | set(minus.keys())
            for k in sorted(keys):
                cur -= minus[k]
                if cur == 0:
                    res += 1
                cur += plus[k]
            return res
        
        res1 = check(xPlus, xMinus)
        res2 = check(yPlus, yMinus)
        return res1 >= 4 or res2 >= 4
# @lc code=end

sol = Solution()
print(sol.checkValidCuts(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))

print(sol.checkValidCuts(4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))

print(sol.checkValidCuts(4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))

#
# @lcpr case=start
# 5\n[[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]\n
# @lcpr case=end

#

