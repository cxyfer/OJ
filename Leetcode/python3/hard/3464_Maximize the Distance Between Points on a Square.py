#
# @lc app=leetcode id=3464 lang=python3
#
# [3464] Maximize the Distance Between Points on a Square
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        n = len(points)

        # w0 
        A = []
        for x, y in points:
            if x == 0:
                A.append(y)
            elif y == side:
                A.append(side + x)
            elif x == side:
                A.append(side * 3 - y)
            elif y == 0:
                A.append(side * 4 - x)
        A.sort()

        def check(mid: int) -> bool:
            # 枚舉第一個點
            # 注意不用考慮循環，因為循環後的點在前面就枚舉過了
            # 如果循環後能找到k個點，則在前面的枚舉就能找到了
            for i in range(n - k + 1):
                cur = A[i]
                for _ in range(k - 1):
                    j = bisect_left(A, cur + mid)
                    if j == len(A):
                        break
                    cur = A[j]
                else:
                    if 4 * side - cur + A[i] >= mid:
                        return True
            return False

        left, right = 0, side
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
# @lc code=end

sol = Solution()
print(sol.maxDistance(side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4))  # 2
print(sol.maxDistance(side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4))  # 1