#
# @lc app=leetcode id=3522 lang=python3
#
# [3522] Calculate Score After Performing Instructions
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        ans = idx = 0
        vis = [False] * n
        while 0 <= idx < n and not vis[idx]:
            vis[idx] = True
            if instructions[idx] == "jump":
                idx += values[idx]
            else:
                ans += values[idx]
                idx += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.calculateScore(["jump","add","add","jump","add","jump"], [2,1,3,1,-2,-3]))  # 1