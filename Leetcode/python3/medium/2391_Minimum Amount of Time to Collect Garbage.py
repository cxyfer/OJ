#
# @lc app=leetcode id=2391 lang=python3
# @lcpr version=30201
#
# [2391] Minimum Amount of Time to Collect Garbage
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Simulation + Prefix Sum(*)
    """
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        m, p, g = 0, 0, 0 # 三台垃圾車的最後位置
        pre = list(accumulate(travel, initial=0)) # 前綴和
        for i, s in enumerate(garbage):
            ans += len(s) # 所有垃圾的收集時間都同樣是 1
            if "M" in s:
                m = i
            if "P" in s:
                p = i
            if "G" in s:
                g = i
        return ans + pre[m] + pre[p] + pre[g] # 到最後位置的行駛時間
# @lc code=end



#
# @lcpr case=start
# ["G","P","GP","GG"]\n[2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# ["MMM","PGM","GP"]\n[3,10]\n
# @lcpr case=end

#

