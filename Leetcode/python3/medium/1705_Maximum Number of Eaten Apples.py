#
# @lc app=leetcode id=1705 lang=python3
# @lcpr version=30204
#
# [1705] Maximum Number of Eaten Apples
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        ans = t = 0
        hp = []
        while t < n or hp:
            if t < n and apples[t] > 0:
                heappush(hp, (t + days[t], apples[t]))
            while hp and hp[0][0] <= t:
                heappop(hp)
            if hp:
                nt, a = heappop(hp)
                ans += 1
                if nt > t and a - 1 > 0:
                    heappush(hp, (nt, a - 1))
            t += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.eatenApples([1,2,3,5,2], [3,2,1,4,2]))  # 7
print(sol.eatenApples([3,0,0,0,0,2], [3,0,0,0,0,2]))  # 5

#
# @lcpr case=start
# [1,2,3,5,2]\n[3,2,1,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,0,0,0,0,2]\n[3,0,0,0,0,2]\n
# @lcpr case=end

#

