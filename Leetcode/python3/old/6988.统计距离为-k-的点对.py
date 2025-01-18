#
# @lc app=leetcode.cn id=6988 lang=python3
#
# [6988] 统计距离为 k 的点对
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        """
            1. Brute Force + Hash Table
            (x1 ^ x2) + (y1 ^ y2) = k
            0 <= (x1 ^ x2) <= k
            0 <= (y1 ^ y2) <= k
            x1 ^ x2 = i
            y1 ^ y2 = k - i
            => x1 ^ x2 ^ x2 = i ^ x2 => x1 = i ^ x2
        """
        ans = 0
        cnt = Counter()
        for x1, y1 in coordinates:
            for i in range(k+1):
                ans += cnt[(x1 ^ i, y1 ^ (k - i))]
            cnt[(x1, y1)] += 1
        return ans  
# @lc code=end

