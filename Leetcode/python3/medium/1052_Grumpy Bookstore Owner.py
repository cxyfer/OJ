#
# @lc app=leetcode id=1052 lang=python3
# @lcpr version=30204
#
# [1052] Grumpy Bookstore Owner
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. Prefix Sum
    2. Sliding Window
"""

class Solution1:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        tot = sum(customers[i] for i in range(n) if not grumpy[i])
        s = [0] * (n+1)
        for i in range(n):
            s[i+1] = s[i] + customers[i] * grumpy[i]
        ans = 0
        for i in range(n - minutes + 1):
            ans = max(ans, s[i+minutes] - s[i])
        return tot + ans
    
class Solution2:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        tot = sum(customers[i] for i in range(n) if not grumpy[i])
        ans = cur = sum(customers[i] * grumpy[i] for i in range(minutes))
        for i in range(minutes, n):
            cur += customers[i] * grumpy[i] - customers[i - minutes] * grumpy[i - minutes]
            ans = max(ans, cur)
        return tot + ans

class Solution(Solution1):
# class Solution(Solution2):
    pass
# @lc code=end




#
# @lcpr case=start
# [1,0,1,2,1,1,7,5]\n[0,1,0,1,0,1,0,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[0]\n1\n
# @lcpr case=end

#

