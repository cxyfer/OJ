#
# @lc app=leetcode.cn id=2103 lang=python3
#
# [2103] 环和杆
#
from preImport import *
# @lc code=start
class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings) // 2
        cnt = [defaultdict(int) for _ in range(10)]
        for i in range(n):
            color, pos = rings[2*i], rings[2*i+1]
            cnt[int(pos)][color] += 1
        ans = 0
        for i in range(10):
            if cnt[i]['R'] > 0 and cnt[i]['G'] > 0 and cnt[i]['B'] > 0:
                ans += 1
        return ans
# @lc code=end

