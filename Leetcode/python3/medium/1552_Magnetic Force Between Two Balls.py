#
# @lc app=leetcode id=1552 lang=python3
# @lcpr version=30204
#
# [1552] Magnetic Force Between Two Balls
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    Sorting + Binary Search
    Same as 2517. Maximum Tastiness of Candy Basket
"""
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def check(d: int) -> bool:
            cnt = 1
            pre = position[0]
            for i in range(1, n):
                if position[i] - pre >= d:
                    cnt += 1
                    pre = position[i]
            return cnt >= m

        left, right = 0, position[-1] - position[0]
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
# [1,2,3,4,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [5,4,3,2,1,1000000000]\n2\n
# @lcpr case=end

#

