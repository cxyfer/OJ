#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#


# @lcpr-template-start
from preImport import *
from operator import add, sub, mul, truediv
# @lcpr-template-end
# @lc code=start
EPS = 1e-6
OPS = [add, sub, mul, truediv, lambda x, y: y - x, lambda x, y: y / x]
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs() -> bool:
            if len(cards) == 1:
                return abs(cards[0] - 24) < EPS
            n = len(cards)
            for i in range(n):
                x = cards.pop(i)
                for j in range(i):
                    y = cards[j]
                    for k, op in enumerate(OPS):
                        if k == 3 and y == 0 or k == 5 and x == 0:
                            continue
                        cards[j] = op(x, y)
                        if dfs():
                            return True
                    cards[j] = y
                cards.insert(i, x)
            return False
        return dfs()
# @lc code=end

sol = Solution()
print(sol.judgePoint24([4, 1, 8, 7]))
print(sol.judgePoint24([1, 2, 1, 2]))