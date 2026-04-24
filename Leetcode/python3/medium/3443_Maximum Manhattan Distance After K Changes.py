#
# @lc app=leetcode id=3443 lang=python3
#
# [3443] Maximum Manhattan Distance After K Changes
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # return (lambda cnt: max((cnt.__setitem__(d, cnt[d] + 1), abs(cnt['N'] - cnt['S']) + abs(cnt['E'] - cnt['W']) + min(k, min(cnt['N'], cnt['S']) + min(cnt['E'], cnt['W'])) * 2)[1] for d in s))(defaultdict(int))
        ans = 0
        cnt = defaultdict(int)
        for d in s:
            cnt[d] += 1
            x = abs(cnt["N"] - cnt["S"])
            y = abs(cnt["E"] - cnt["W"])
            t1 = min(cnt["N"], cnt["S"])
            t2 = min(cnt["E"], cnt["W"])
            ans = max(ans, x + y + (min(k, t1 + t2) << 1))
        return ans
# @lc code=end

