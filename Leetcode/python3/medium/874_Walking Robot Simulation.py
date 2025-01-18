#
# @lc app=leetcode id=874 lang=python3
# @lcpr version=30204
#
# [874] Walking Robot Simulation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x, y, d = 0, 0, 0
        st = set([(x, y) for x, y in obstacles])
        ans = 0
        for command in commands:
            if command < 0:
                d = (d + (1 if command == -1 else -1)) % 4
            else:
                for _ in range(command):
                    if (x + DIRS[d][0], y + DIRS[d][1]) in st:
                        break
                    x, y = x + DIRS[d][0], y + DIRS[d][1]
                    ans = max(ans, x * x + y * y)
        return ans
# @lc code=end

#
# @lcpr case=start
# [4,-1,3]\n[]\n
# @lcpr case=end

# @lcpr case=start
# [4,-1,4,-2,4]\n[[2,4]]\n
# @lcpr case=end

# @lcpr case=start
# [6,-1,-1,6]\n[]\n
# @lcpr case=end

#

