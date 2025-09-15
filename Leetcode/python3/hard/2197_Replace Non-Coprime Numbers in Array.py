#
# @lc app=leetcode id=2197 lang=python3
#
# [2197] Replace Non-Coprime Numbers in Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        for x in nums:
            while st and math.gcd(st[-1], x) > 1:
                x = math.lcm(st.pop(), x)
            st.append(x)
        return st
# @lc code=end
sol = Solution()
print(sol.replaceNonCoprimes([6,4,3,2,7,6,2]))  # [12,7,6]
