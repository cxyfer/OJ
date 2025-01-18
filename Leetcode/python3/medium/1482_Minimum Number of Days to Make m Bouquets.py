#
# @lc app=leetcode id=1482 lang=python3
# @lcpr version=30204
#
# [1482] Minimum Number of Days to Make m Bouquets
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        # check if we can make m bouquets with k flowers in d days
        def check(d: int):
            res = cur = 0 # res: number of bouquets, cur: number of adjacent flowers
            for bloom in bloomDay:
                if bloom <= d:
                    cur += 1
                    if cur == k:
                        res += 1
                        cur = 0
                else: # not adjacent
                    cur = 0
            return res >= m
        
        left, right = min(bloomDay), max(bloomDay)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left if left <= max(bloomDay) else -1
# @lc code=end



#
# @lcpr case=start
# [1,10,3,10,2]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,10,3,10,2]\n3\n2\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,12,7,7]\n2\n3\n
# @lcpr case=end

#

