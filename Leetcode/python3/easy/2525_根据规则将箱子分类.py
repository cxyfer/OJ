#
# @lc app=leetcode.cn id=2525 lang=python3
#
# [2525] 根据规则将箱子分类
#

# @lc code=start
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        isBulky = any(dimension >= 10**4 for dimension in [length, width, height]) or length * width * height >= 10**9
        isHeavy = mass >= 100
        if isBulky and isHeavy:
            return "Both"
        elif isBulky:
            return "Bulky"
        elif isHeavy:
            return "Heavy"
        else:
            return "Neither"
# @lc code=end

