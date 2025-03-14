#
# @lc app=leetcode.cn id=3356 lang=python3
# @lcpr version=30204
#
# [3356] 零数组变换 II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        def check(k):
            diff = [0] * (n + 1)
            for l, r, v in queries[:k]:
                diff[l] += v
                diff[r + 1] -= v
            for i in range(1, n + 1):
                diff[i] += diff[i - 1]
            return all(x <= d for x, d in zip(nums, diff))
        left, right = 0, m
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left if left <= m else -1
    
class Solution(Solution1):
    pass
# @lc code=end

sol = Solution()
print(sol.minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]))  # 2
print(sol.minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]]))  # -1
print(sol.minZeroArray([10], [[0,0,5],[0,0,3],[0,0,2],[0,0,1],[0,0,4],[0,0,1],[0,0,4],[0,0,5],[0,0,3],[0,0,4],[0,0,1]]))  # 3

#
# @lcpr case=start
# [2,0,2]\n[[0,2,1],[0,2,1],[1,1,3]]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n[[1,3,2],[0,2,1]]\n
# @lcpr case=end

#

