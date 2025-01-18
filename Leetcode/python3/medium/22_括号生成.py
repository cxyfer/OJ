#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from preImport import *
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []
        def dfs(i):
            if i == n * 2:
                ans.append(''.join(path))
                return
            if path.count('(') < n:
                path.append('(')
                dfs(i + 1)
                path.pop()
            if path.count(')') < path.count('('):
                path.append(')')
                dfs(i + 1)
                path.pop()
        dfs(0)
        return ans
# @lc code=end
sol = Solution()
print(sol.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
