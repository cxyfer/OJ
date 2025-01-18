# @algorithm @lc id=22 lang=python3 
# @title generate-parentheses


from en.Python3.mod.preImport import *
# @test(3)=["((()))","(()())","(())()","()(())","()()()"]
# @test(1)=["()"]
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