#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 行星碰撞
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            if a > 0:
                st.append(a)
            else:
                if st and st[-1] == -a: # same size
                    st.pop()
                    continue
                while st and st[-1] > 0 and st[-1] < -a:
                    st.pop()
                if not st or st[-1] < 0:
                    st.append(a)
                elif st[-1] == -a:
                    st.pop()
        return st
# @lc code=end
sol = Solution()
print(sol.asteroidCollision([-2,2,1,-2])) # [-2]

