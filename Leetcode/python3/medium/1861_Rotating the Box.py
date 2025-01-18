#
# @lc app=leetcode id=1861 lang=python3
# @lcpr version=30204
#
# [1861] Rotating the Box
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n, m = len(box), len(box[0])
        ans = [["."] * n for _ in range(m)]
        for i, row in enumerate(box):
            cnt = 0
            for j, ch in enumerate(row):
                if ch == "#":
                    cnt += 1
                elif ch == "*":
                    for k in range(cnt):
                        ans[j - 1 - k][n - 1 - i] = "#"
                    ans[j][n - 1 - i] = "*"
                    cnt = 0
            for k in range(cnt):
                ans[m - 1 - k][n - 1 - i] = "#"
        return ans
# @lc code=end

sol = Solution()
print(sol.rotateTheBox([["#",".","#"]])) # 	[[“.”],["#"],["#"]]

#
# @lcpr case=start
# [["#",".","#"]]\n
# @lcpr case=end

# @lcpr case=start
# [["#",".","*","."],["#","#","*","."]]\n
# @lcpr case=end

# @lcpr case=start
# [["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]\n
# @lcpr case=end

#

