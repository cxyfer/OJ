#
# @lc app=leetcode id=502 lang=python3
# @lcpr version=30203
#
# [502] IPO
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(c, p) for c, p in zip(capital, profits)]
        projects.sort() # Sort the projects by capital in ascending order

        ans, idx = w, 0
        hp = [] # Max heap
        for _ in range(k):
            while idx < n and projects[idx][0] <= ans: # Add all the projects that can be done now
                heappush(hp, -projects[idx][1]) # Max heap
                idx += 1
            if not hp: # No project can be done
                break
            ans += -heappop(hp) # Do the project with the maximum profit
        return ans
# @lc code=end



#
# @lcpr case=start
# 2\n0\n[1,2,3]\n[0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# 3\n0\n[1,2,3]\n[0,1,2]\n
# @lcpr case=end

#

