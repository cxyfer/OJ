#
# @lc app=leetcode id=241 lang=python3
# @lcpr version=30204
#
# [241] Different Ways to Add Parentheses
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        tokens = []
        idx = 0
        num = 0
        while idx < n:
            if expression[idx].isdigit():
                num = 0
                while idx < n and expression[idx].isdigit():
                    num = num * 10 + int(expression[idx])
                    idx += 1
                tokens.append(num)
            else:
                tokens.append(expression[idx])
                idx += 1
        
        m = len(tokens)

        @cache
        def dfs(l, r):
            if l == r:
                return [tokens[l]]
            res = []
            for i in range(l, r, 2):
                op = tokens[i + 1]
                left = dfs(l, i)
                right = dfs(i + 2, r)
                for x in left:
                    for y in right:
                        if op == '+':
                            res.append(x + y)
                        elif op == '-':
                            res.append(x - y)
                        elif op == '*':
                            res.append(x * y)
            return res
        return dfs(0, m - 1)
# @lc code=end

sol = Solution()
print(sol.diffWaysToCompute("2-1-1"))
print(sol.diffWaysToCompute("2*3-4*5"))
print(sol.diffWaysToCompute("11"))

#
# @lcpr case=start
# "2-1-1"\n
# @lcpr case=end

# @lcpr case=start
# "2*3-4*5"\n
# @lcpr case=end

#

