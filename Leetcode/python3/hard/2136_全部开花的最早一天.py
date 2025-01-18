#
# @lc app=leetcode.cn id=2136 lang=python3
#
# [2136] 全部开花的最早一天
#
from preImport import *
# @lc code=start
class Solution:
    """
        Greedy
        plantTime的總和是固定的，因此貪婪的思路是盡可能先種growTime長的花
    """
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = 0
        cur = 0 # 當前時間
        for pt, gt in sorted(zip(plantTime, growTime), key=lambda x:x[1], reverse=True):
            cur += pt # 種植完成的時間
            ans = max(ans, cur + gt) # 若當前花開的時間比答案還晚，則更新答案
        return ans
# @lc code=end

