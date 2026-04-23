#
# @lc app=leetcode id=2615 lang=python3
#
# [2615] Sum of Distances
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)
        for i, x in enumerate(nums):
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

