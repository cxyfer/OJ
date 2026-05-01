#
# @lc app=leetcode id=2121 lang=python3
#
# [2121] Intervals Between Identical Elements
#

"""
本題同 2615. Sum of Distances
"""

# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        pos = defaultdict(list)
        for i, x in enumerate(arr):
            pos[x].append(i)
        
        ans = [0] * n
        for x, idxs in pos.items():
            m = len(idxs)
            # s = list(accumulate(idxs, initial=0))
            pre = 0
            suf = sum(idxs)
            for i, idx in enumerate(idxs, start=1):
                # L = idx * (i - 1) - s[i - 1]
                # R = (s[m] - s[i]) - idx * (m - i)
                suf -= idx
                L = idx * (i - 1) - pre
                R = suf - idx * (m - i)
                ans[idx] = L + R
                pre += idx
        return ans
# @lc code=end

