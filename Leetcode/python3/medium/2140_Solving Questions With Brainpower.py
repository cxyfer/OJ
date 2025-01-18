#
# @lc app=leetcode id=2140 lang=python3
# @lcpr version=30204
#
# [2140] Solving Questions With Brainpower
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @cache
        def f(i: int) -> int: # 從第 i 個問題開始考慮最多可以獲得多少分數
            if i >= n:
                return 0
            res1 = f(i + 1) # 不選第 i 個問題
            res2 = questions[i][0] + f(i + questions[i][1] + 1) # 選第 i 個問題
            return max(res1, res2)
        return f(0)
    
class Solution2:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        f = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            f[i] = max(f[i + 1], questions[i][0] + f[min(i + questions[i][1] + 1, n)])
        return f[0]
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.mostPoints([[3,2],[4,3],[4,4],[2,5]])) # 5
print(sol.mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]])) # 7

#
# @lcpr case=start
# [[3,2],[4,3],[4,4],[2,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,2],[3,3],[4,4],[5,5]]\n
# @lcpr case=end

#

