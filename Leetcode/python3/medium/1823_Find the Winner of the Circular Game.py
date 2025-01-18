#
# @lc app=leetcode id=1823 lang=python3
# @lcpr version=30204
#
# [1823] Find the Winner of the Circular Game
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. Simulation + Queue
    2. Math + Recursion
       Josephus problem
         - (0-based): f(n, k) = (f(n-1, k) + k) % n
            base case: f(1, k) = 0
         - (1-based): f(n, k) = (f(n-1, k) + k - 1) % n + 1
            base case: f(1, k) = 1
    3. Math + Iteration
"""

class Solution1:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque(range(1, n+1))
        while len(q) > 1:
            for _ in range(k-1):
                q.append(q.popleft())
            q.popleft()
        return q[0]

class Solution2:
    def findTheWinner(self, n: int, k: int) -> int:
        return 1 if n == 1 else (self.findTheWinner(n-1, k) + k - 1) % n + 1

class Solution3:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 1
        for i in range(2, n+1):
            ans = (ans + k - 1) % i + 1
        return ans
    
# class Solution(Solution1):
# class Solution(Solution2):
class Solution(Solution3):
    pass
# @lc code=end

#
# @lcpr case=start
# 5\n2\n
# @lcpr case=end

# @lcpr case=start
# 6\n5\n
# @lcpr case=end

#

