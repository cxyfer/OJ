#
# @lc app=leetcode id=3449 lang=python3
# @lcpr version=30204
#
# [3449] Maximize the Minimum Game Score
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Reference: 
- https://sua.ac/wiki/2018-icpc-qingdao/e/
- https://leetcode.cn/problems/maximize-the-minimum-game-score/solutions/3068672/er-fen-da-an-cong-zuo-dao-you-tan-xin-py-3bhl
"""
# @lc code=start
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def check(k: int) -> bool:
            cnt = pre = 0
            for p in points:
                x = pre * p
                if x < k:
                    t = math.ceil((k - x) / p)  # 還需要 t 次操作
                    cnt += t * 2 - 1
                    if cnt > m:
                        return False
                    pre = t - 1  # 右邊的數操作了 t - 1 次
                else:
                    cnt += 1
                    pre = 0
            return True
        
        left, right = 0, m * min(points)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
# @lc code=end
sol = Solution()
print(sol.maxScore([2, 4], 3))  # 4
print(sol.maxScore([1, 2, 3], 5))  # 2
print(sol.maxScore([4,2], 9))  # 8
print(sol.maxScore([2,5], 2))  # 2


#
# @lcpr case=start
# [2,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

#

