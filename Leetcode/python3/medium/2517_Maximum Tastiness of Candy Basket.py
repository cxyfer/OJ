#
# @lc app=leetcode id=2517 lang=python3
# @lcpr version=30204
#
# [2517] Maximum Tastiness of Candy Basket
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    Sorting + Binary Search
    Same as 1552. Magnetic Force Between Two Balls
"""
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        n = len(price)
        price.sort()

        def check(d: int) -> bool:
            cnt = 1
            pre = price[0]
            for i in range(1, n):
                if price[i] - pre >= d:
                    cnt += 1
                    pre = price[i]
            return cnt >= k

        left, right = 0, price[-1] - price[0]
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
# @lc code=end



#
# @lcpr case=start
# [13,5,1,8,21,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,3,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7]\n2\n
# @lcpr case=end

#

